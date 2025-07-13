import pytest
from pages.admin_page import AdminPage


def test_print_usernames(login, user_data):
    if user_data["is_valid"]:
        admin = AdminPage(login)

        # Step 1: Navigate to Admin tab
        admin.click_admin_tab()

        # Step 2: Get usernames without clicking search
        usernames = admin.get_user_column_texts()

        # Step 3: Print usernames
        print("\n--- Usernames Listed on Admin Page ---")
        for name in usernames:
            print(name)

        # Optional assert
        assert len(usernames) > 0, "No users found on Admin page"
