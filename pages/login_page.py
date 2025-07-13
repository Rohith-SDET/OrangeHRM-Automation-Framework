from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard_text = (By.CSS_SELECTOR, ".oxd-topbar-header-breadcrumb > h6")  # Text shown after successful login
        self.invalid_cred = (By.XPATH, "//p[text()='Invalid credentials']")

    # Method to enter username
    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    # Method to enter password
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    # Method to click login
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    # Combined method to login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Get the dashboard text after successful login
    def get_dashboard_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_text)).text

    # Get error message after failed login
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.invalid_cred)).text
