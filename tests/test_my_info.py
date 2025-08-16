import pytest
import json
import os
from pages.my_info_page import MyInfoPage
from pages.login_page import LoginPage


def load_myinfo_test_data(filepath="data/my_info_test_data.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)["information"]


@pytest.mark.parametrize("record", load_myinfo_test_data())
def test_update_personal_info(driver, record):
    # Login
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    # Navigate and update personal details
    my_info = MyInfoPage(driver)
    my_info.click_my_info_tab()
    my_info.enter_first_name(record["first_name"])
    my_info.enter_middle_name(record["middle_name"])
    my_info.enter_last_name(record["last_name"])
    my_info.enter_emp_id(record["emp_id"])
    my_info.enter_other_id(record["other_id"])
    my_info.enter_driver_licence(record["driver_licence"])
    my_info.enter_licence_exp_date(record["licence_exp_date"])
    my_info.select_nationality(record["nationality"])
    my_info.select_marital_status(record["marital_status"])
    my_info.enter_date_of_birth(record["date_of_birth"])
    my_info.select_gender(record["first_name"])
    my_info.click_save_button()
    my_info.assert_success_message()
