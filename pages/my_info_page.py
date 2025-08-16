from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Your absolute XPaths as provided
        self.my_info_tab = (By.XPATH, "//span[text()='My Info']")
        self.employee_first_name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input")
        self.employee_middle_name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input")
        self.employee_last_name = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input")
        self.emp_id = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input")
        self.other_id = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input")
        self.driver_licence = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input")
        self.licence_exp_date = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input")
        self.nationality = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div")
        self.marital_status = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div")
        self.date_of_birth = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")
        self.gender_male = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label")
        self.gender_female = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label")
        self.save_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button")
        self.toast_title = (By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]")

    def click_my_info_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.my_info_tab)).click()

    def clear_and_fill(self, locator, value):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].removeAttribute('readonly')", field)
        self.driver.execute_script("arguments[0].removeAttribute('disabled')", field)
        self.driver.execute_script("arguments[0].value = '';", field)
        self.driver.execute_script("arguments[0].value = arguments[1];", field, value)
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", field)

    def enter_first_name(self, value):
        self.clear_and_fill(self.employee_first_name, value)

    def enter_middle_name(self, value):
        self.clear_and_fill(self.employee_middle_name, value)

    def enter_last_name(self, value):
        self.clear_and_fill(self.employee_last_name, value)

    def enter_emp_id(self, value):
        self.clear_and_fill(self.emp_id, value)

    def enter_other_id(self, value):
        self.clear_and_fill(self.other_id, value)

    def enter_driver_licence(self, value):
        self.clear_and_fill(self.driver_licence, value)

    def enter_licence_exp_date(self, value):
        self.clear_and_fill(self.licence_exp_date, value)

    def select_nationality(self, nationality_value):
        self.wait.until(EC.element_to_be_clickable(self.nationality)).click()
        option = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//div[@role='listbox']//span[text()='{nationality_value}']")
        ))
        option.click()

    def select_marital_status(self, marital_status_value):
        self.wait.until(EC.element_to_be_clickable(self.marital_status)).click()
        option = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//div[@role='listbox']//span[text()='{marital_status_value}']")
        ))
        option.click()

    def enter_date_of_birth(self, value):
        self.clear_and_fill(self.date_of_birth, value)

    def select_gender(self, first_name):
        boys = {'arjun', 'krishna', 'michael', 'john', 'david', 'robert', 'james'}
        girls = {'anbarasi', 'mary', 'linda', 'geetha', 'priya', 'lakshmi', 'jessica'}
        key = first_name.strip().split()[0].lower()
        if key in boys:
            self.wait.until(EC.element_to_be_clickable(self.gender_male)).click()
        elif key in girls:
            self.wait.until(EC.element_to_be_clickable(self.gender_female)).click()
        else:
            raise ValueError(f"Unknown gender for the name '{first_name}' (please extend the logic).")

    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def assert_success_message(self):
        elem = self.wait.until(EC.visibility_of_element_located(self.toast_title))
        assert "success" in elem.text.lower()
