import pytest
import json
from pages.performance_page import PerformanceKPIPage
from pages.login_page import LoginPage

def load_kpi_test_data(filepath="data/performance_test_data.json"):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)["kpis"]

@pytest.mark.parametrize("record", load_kpi_test_data())
def test_add_kpi(driver, record):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    kpi_page = PerformanceKPIPage(driver)
    kpi_page.goto_kpi_management()
    kpi_page.add_kpi(
        record["kpi_name"],
        record["job_title"],
        record["min_rating"],
        record["max_rating"],
        record.get("make_default", False)
    )
    kpi_page.assert_success()
    #
    # kpi_page.select_job_title_search(record["job_title"])
    # expect_yes = record.get("make_default", False)
    # assert kpi_page.verify_kpi_row_with_yes_state(
    #     record["kpi_name"], record["job_title"], expect_yes
    # ), f"KPI '{record['kpi_name']}' with 'Yes'={expect_yes} and '{record['job_title']}' role not found correctly"
