from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Absolute XPaths for reliability in OrangeHRM
        self.recruitment_tab = (By.XPATH, "//a[contains(@class, 'oxd-main-menu-item') and contains(., 'Recruitment')]")
        self.vacancies_tab = (By.XPATH, "//a[contains(@class, 'oxd-topbar-body-nav-tab-item') and contains(., 'Vacancies')]")
        self.add_vacancy_button = (By.XPATH, "//button[contains(., 'Add')]")

        self.job_title_dropdown = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/div/div")
        self.job_title_options = (By.XPATH, "//div[@role='listbox']//span")
        self.vacancy_name_input = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
        self.description_textarea = (By.XPATH, "//textarea[@placeholder='Type description here']")
        self.hiring_manager_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.no_of_positions_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/form/div[3]/div[2]/div/div/div/div[2]/input")

        self.save_button = (By.XPATH, "//button[contains(., 'Save')]")
        # self.toast_title = (By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]")






    def click_recruitment_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.recruitment_tab)).click()

    def open_vacancies_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.vacancies_tab)).click()

    def click_add_vacancy(self):
        self.wait.until(EC.element_to_be_clickable(self.add_vacancy_button)).click()

    def select_job_title(self, job_title):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown))
        dropdown.click()
        options = self.wait.until(EC.presence_of_all_elements_located(self.job_title_options))
        for option in options:
            if option.text.strip() == job_title:
                # self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
                ActionChains(self.driver).move_to_element(option).click().perform()
                break
        time.sleep(1)  # let UI update after selection
        self.wait.until(EC.visibility_of_element_located(self.vacancy_name_input))

    def enter_vacancy_name(self, vacancy_name):
        elem = self.wait.until(EC.visibility_of_element_located(self.vacancy_name_input))
        elem.clear()
        elem.send_keys(vacancy_name)

    def enter_description(self, description):
        elem = self.wait.until(EC.visibility_of_element_located(self.description_textarea))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()
        time.sleep(0.2)
        elem.send_keys(description)

    def enter_hiring_manager(self, manager_name):
        elem = self.wait.until(EC.element_to_be_clickable(self.hiring_manager_input))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", elem)
        elem.click()
        time.sleep(0.3)
        elem.send_keys(manager_name)
        options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span")))
        # Find and click the exact visible text match
        for option in options:
            if option.text.strip() == manager_name:
                # self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
                ActionChains(self.driver).move_to_element(option).click().perform()
                break

    def enter_number_of_positions(self, number):
        elem = self.wait.until(EC.visibility_of_element_located(self.no_of_positions_input))
        elem.clear()
        elem.send_keys(str(number))

    def save_vacancy(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()
        time.sleep(10)


    # def assert_success_message(self):
    #     elem = self.wait.until(EC.visibility_of_element_located(self.toast_title))
    #     assert "success" in elem.text.lower()
    # def assert_success_message(self, expected_text="Success"):
    #     elem = WebDriverWait(self.driver, 5).until(
    #         EC.presence_of_element_located(self.success_message))
    #     actual_text = elem.self.success_message
    #     assert expected_text() in actual_text, f"Expected '{expected_text}' in '{actual_text}'"
    #     # assert "success" in success_message
