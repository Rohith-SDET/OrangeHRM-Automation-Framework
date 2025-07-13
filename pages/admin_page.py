from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.admin_tab = (By.XPATH, "//span[text()='Admin']")
        self.header = (By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
        # self.username_input = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        # self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        # self.user_name_input = (By.XPATH, "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--active']")
        # self.user_role_dropdown = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]")
        # self.status_dropdown = (By.XPATH, "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]")
        # self.search_button = (By.XPATH, "//button[@type='submit']")
        # self.no_records = (By.XPATH, "//span[text()='No Records Found']")
        # self.table_rows = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
        self.user_column = (By.XPATH, "//div[@class='oxd-table-cell oxd-padding-cell'][2]")

    # Clicks on the Admin tab in the sidebar
    def click_admin_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_tab)
        ).click()

    # Returns the page header text (used to verify "Admin" page loaded)
    def get_header_text(self):
        return self.driver.find_element(*self.header).text

    # Returns a list of all usernames from the user table
    def get_user_column_texts(self):
        """Get all usernames from the Admin table."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.user_column)
        )
        rows = self.driver.find_elements(*self.user_column)
        return [row.text for row in rows if row.text.strip() != ""]

    # Enters a username into the search field
    # def enter_username(self, username):
    #     self.driver.find_element(*self.username_input).clear()
    #     self.driver.find_element(*self.username_input).send_keys(username)
    #
    # # Clicks the Search button
    # def click_search(self):
    #     self.driver.find_element(*self.search_button).click()
    #
    # # Clicks the Reset button
    # def click_reset(self):
    #     self.driver.find_element(*self.reset_button).click()
    #
    # # Checks whether any records were found in the search results
    # def is_result_found(self):
    #     return len(self.driver.find_elements(*self.no_records)) == 0
    #
    # # Generic dropdown selector (for User Role and Status)
    # def select_from_dropdown(self, dropdown_locator, value):
    #     self.driver.find_element(*dropdown_locator).click()
    #     options = self.driver.find_elements(*self.dropdown_options)
    #     for option in options:
    #         if option.text.strip() == value:
    #             option.click()
    #             break
