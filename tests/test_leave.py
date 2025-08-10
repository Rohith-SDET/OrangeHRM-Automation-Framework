import pytest
from pages.login_page import LoginPage
from pages.leave_page import LeavePage

def test_apply_leave_no_balance(driver):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    leave = LeavePage(driver)
    leave.navigate_to_apply_tab()

    message = leave.get_no_leave_message()

    assert message == "No Leave Types with Leave Balance", f" Unexpected leave message: {message}"
    print("Correct message displayed when no leave balance is available.")
