# pages/time_attendance_page.py

from selenium.webdriver.common.by import By

class TimeAttendancePage:
    def __init__(self, driver):
        self.driver = driver

    # Locators (example, change as per your app selectors)
    time_menu = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span")
    timesheet_tab = (By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")
    # my_timesheet_option = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a")
    timesheet_text = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/h6")

    # Methods
    def navigate_to_time_module(self):
        self.driver.find_element(*self.time_menu).click()

    def navigate_to_timesheet_tab(self):
        self.driver.find_element(*self.timesheet_tab).click()

    # def navigate_to_my_timesheet(self):
    #     self.driver.find_element(*self.my_timesheet_option).click()

    def verify_timesheet_page(self):
        return self.driver.find_element(*self.timesheet_text).text
