import pytest
<<<<<<< HEAD
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
=======
import json
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

# Load JSON test data
def load_test_data():
    with open("data/tes_data_admin.json", "r") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
def test_admin_search_user(driver, data):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    admin = AdminPage(driver)
    admin.go_to_admin()

    admin.search_user(
        username=data["username"],
        userrole=data["userrole"],
        employee=data["employee"],
        status=data["status"]
    )

    print(f"\n🔍Search for: {data['username']} ({data['employee']})")
    admin.print_results()
>>>>>>> e0eb84e (Initial commit)
