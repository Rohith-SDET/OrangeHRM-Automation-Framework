from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.pim_menu = (By.XPATH, "//span[text()='PIM']")
        self.add_button = (By.XPATH, "//button[normalize-space()='Add']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.employee_id_input = (By.XPATH, "//label[text()='Employee Id']/../following-sibling::div/input")
        self.save_button = (By.XPATH, "//button[normalize-space()='Save']")
        self.employee_list_tab = (By.LINK_TEXT, "Employee List")
        self.employee_name_search = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.no_records_label = (By.XPATH, "//span[text()='No Records Found']")

    def go_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_menu)).click()

    def add_employee(self, first_name, last_name, employee_id):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        self.wait.until(EC.presence_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

        emp_id_elem = self.driver.find_element(*self.employee_id_input)
        emp_id_elem.clear()
        emp_id_elem.send_keys(employee_id)

        self.driver.find_element(*self.save_button).click()

    def search_employee(self, name):
        self.wait.until(EC.element_to_be_clickable(self.employee_list_tab)).click()
        self.wait.until(EC.presence_of_element_located(self.employee_name_search)).send_keys(name)
        self.driver.find_element(*self.search_button).click()

    def is_no_record_found(self):
        return len(self.driver.find_elements(*self.no_records_label)) > 0
