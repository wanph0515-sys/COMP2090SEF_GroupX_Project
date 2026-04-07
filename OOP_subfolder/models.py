from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id: str, title: str):
        self.itemid = item_id
        self.title = title
        self.isborrowed = False

    def item_id(self):
        return self.itemid

    def title(self):
        return self.title

    def is_borrowed(self):
        return self.isborrowed

    def is_borrowed(self, status: bool):
        self.isborrowed = status

    def get_item_type(self) -> str:
        pass

    def __str__(self):
        status = "Borrowed" if self.isborrowed else "Available"
        return f"[{self.itemid}] {self.title} ({self.get_item_type()}) - {status}"


class Book(LibraryItem):
    def __init__(self, book_id: str, title: str, author: str):
        super().__init__(book_id, title)
        self.author = author

    def author(self):
        return self.author

    def get_item_type(self) -> str:
        return "Book"

    def __str__(self):
        return f"[{self.itemid}] {self.title} by {self.author} - {'Borrowed' if self.isborrowed else 'Available'}"


class User:
    def __init__(self, user_id: str, name: str):
        self.userid = user_id
        self.name = name
        self.borroweditems = []

    def user_id(self):
        return self.userid

    def name(self):
        return self.name

    def borrowed_items(self):
        return self.borroweditems.copy()

    def borrow_item(self, item: LibraryItem):
        if item not in self.borroweditems and not item.isborrowed:
            self.borroweditems.append(item)
            item.isborrowed = True
            return True
        return False

    def return_item(self, item: LibraryItem):
        if item in self.borroweditems:
            self.borroweditems.remove(item)
            item.isborrowed = False
            return True
        return False

    def __str__(self):
        return f"User: {self.name} (ID: {self.userid}), Borrowed: {len(self.borroweditems)} items"


class StaffUser(User):
    def __init__(self, user_id: str, name: str, department: str):
        super().__init__(user_id, name)
        self.department = department

    def department(self):
        return self.department

    def borrow_item(self, item: LibraryItem) -> bool:
        print(f"[Staff] {self.name} is borrowing an item.")
        return super().borrow_item(item)

    def __str__(self):
        return f"Staff: {self.name} (ID: {self.userid}, Dept: {self.department}), Borrowed: {len(self.borroweditems)} items"
