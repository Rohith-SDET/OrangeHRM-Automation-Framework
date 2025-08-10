import pytest
import json
from pages.login_page import LoginPage
from pages.pim_page import PimPage

def load_pim_data():
    with open("data/test_data_pim.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_pim_data())
def test_add_and_search_employee(driver, data):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    pim = PimPage(driver)
    pim.go_to_pim()
    pim.add_employee(data["first_name"], data["last_name"], data["employee_id"])

    pim.search_employee(data["search_name"])
    assert not pim.is_no_record_found(), f" Employee {data['search_name']} not found!"
