from library import Library
from models import Book, User, StaffUser
from utils import IDValidator

def display_menu():
    print("\nLibrary Management System")
    print("1. List all items")
    print("2. Search items")
    print("3. Borrow an item")
    print("4. Return an item")
    print("5. List all users")
    print("6. Add new book")
    print("7. Register new user")
    print("0. Exit")

def main():
    lib = Library.create_preloaded_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            items = lib.list_all_items()
            for item in items:
                print(item)
        elif choice == "2":
            keyword = input("Enter search keyword (title/author): ")
            results = lib.search_items(keyword)
            if results:
                for r in results:
                    print(r)
            else:
                print("No matching items found.")
        elif choice == "3":
            uid = input("Enter User ID: ")
            iid = input("Enter Item ID: ")
            if not IDValidator.is_valid_user_id(uid) or not IDValidator.is_valid_item_id(iid):
                print("Invalid ID format.")
            else:
                success, msg = lib.borrow_item(uid, iid)
                print(msg)
        elif choice == "4":
            uid = input("Enter User ID: ")
            iid = input("Enter Item ID: ")
            success, msg = lib.return_item(uid, iid)
            print(msg)
        elif choice == "5":
            users = lib.list_all_users()
            for u in users:
                print(u)
        elif choice == "6":
            bid = input("Enter Book ID (e.g., B004): ")
            title = input("Title: ")
            author = input("Author: ")
            success, msg = lib.add_item(Book(bid, title, author))
            print(msg)
        elif choice == "7":
            uid = input("Enter User ID (e.g., U003): ")
            name = input("Name: ")
            is_staff = input("Is staff? (y/n): ").lower() == 'y'
            if is_staff:
                dept = input("Department: ")
                user = StaffUser(uid, name, dept)
            else:
                user = User(uid, name)
            success, msg = lib.register_user(user)
            print(msg)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
