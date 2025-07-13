import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("test_case", range(3))  # We have 3 testcases in JSON
def test_login_cases(setup, load_test_data, test_case):
    driver = setup
    data = load_test_data[test_case]
    login = LoginPage(driver)

    print(f"Running: {data['testcase']}")

    # Step 1: Login

    login.login(data["username"], data["password"])

    # Step 2: Validation
    if data["is_valid"]:
        assert data["expected_text"] in login.get_dashboard_text()
        print("✅ Valid login passed.")
    else:
        assert data["expected_text"] in login.get_error_message()
        print("✅ Invalid login handled.")
