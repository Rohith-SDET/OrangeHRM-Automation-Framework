from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LeavePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Navigation locators
        self.leave_menu = (By.XPATH, "//span[text()='Leave']/ancestor::a")
        self.apply_tab = (By.XPATH, "//a[normalize-space()='Apply']")  # more reliable than full XPath

        # Message paragraph element that shows the "No Leave Types..." text
        self.no_leave_text = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")

    def navigate_to_apply_tab(self):
        # Navigate to Leave > Apply
        self.wait.until(EC.element_to_be_clickable(self.leave_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.apply_tab)).click()
        print("Navigated to Apply Leave page.")

    def get_no_leave_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.no_leave_text))
            actual_text = element.text
            print("Leave Info Message: ", actual_text)
            return actual_text
        except TimeoutException:
            print("Message not found.")
            return None
