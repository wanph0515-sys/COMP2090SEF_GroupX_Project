class IDValidator:
    def is_valid_user_id(uid: str) -> bool:
        return uid.startswith("U") and len(uid) == 4 and uid[1:].isdigit()

    def is_valid_item_id(iid: str) -> bool:
        return iid.startswith(("B", "D")) and len(iid) == 4 and iid[1:].isdigit()

    def generate_demo_report(library):
        print("\n===== Library Report =====")
        print(f"Total items: {len(library)}")
        print(f"Total users: {len(library.list_all_users())}")
        borrowed_count = sum(1 for item in library.list_all_items() if item.is_borrowed)
        print(f"Borrowed items: {borrowed_count}")
