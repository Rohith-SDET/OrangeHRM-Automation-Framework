import json
import pytest
from pages.login_page import LoginPage
from pages.recruitment_page import RecruitmentPage
import time

def load_test_data(filepath="data/recruitement_test_data.json"):
    with open(filepath, "r") as file:
        return json.load(file)["vacancies"]

@pytest.mark.parametrize("vacancy", load_test_data())
def test_add_vacancy_and_search_candidates(driver, vacancy):
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    recruitment = RecruitmentPage(driver)
    recruitment.click_recruitment_tab()
    recruitment.open_vacancies_tab()
    recruitment.click_add_vacancy()

    recruitment.select_job_title(vacancy["job_title"])

    # Small wait to allow UI to update after job title selection
    time.sleep(1)

    recruitment.enter_vacancy_name(vacancy["vacancy_name"])

    recruitment.enter_description(vacancy["description"])

    recruitment.enter_hiring_manager(vacancy["hiring_manager"])

    recruitment.enter_number_of_positions(vacancy["number_of_positions"])

    if "job_location" in vacancy:
        recruitment.select_job_location(vacancy["job_location"])

    if "status_active" in vacancy:
        recruitment.set_status_active(vacancy["status_active"])

    if "published" in vacancy:
        recruitment.set_published(vacancy["published"])

    recruitment.save_vacancy()
    # recruitment.assert_success_message()
    # recruitment.assert_success_message("success")
    # # assert recruitment.get_vacancy_text() == vacancy["vacancy_name"], "Vacancy not added correctly"
