from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PerformanceKPIPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.performance_menu = (By.XPATH, "//span[text()='Performance']")
        self.configure_tab = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]")
        self.kpi_submenu = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]/a")
        self.add_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
        self.kpi_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input")
        self.job_title_dropdown = (By.XPATH, "//label[contains(text(), 'Job Title')]/following::div[contains(@class,'oxd-select-wrapper')]")
        self.job_title_option = lambda title: (By.XPATH, f"//div[@role='option']/span[text()='{title}']")
        self.min_rating_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
        self.max_rating_input = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")
        self.default_scale_switch = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div/label/span")
        self.save_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]")
        self.toast_message = (By.XPATH, "//*[@id='oxd-toaster_1']/div/div[1]/div[2]/p[1]")
        self.job_role = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div/div/div[2]/div/div")
        self.search_button = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        # self.kpi_table = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]")



    def goto_kpi_management(self):
        self.wait.until(EC.element_to_be_clickable(self.performance_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.configure_tab)).click()
        self.wait.until(EC.element_to_be_clickable(self.kpi_submenu)).click()

    def clear_and_fill(self, field, value):
        self.driver.execute_script("arguments[0].value = '';", field)
        self.driver.execute_script("arguments[0].value = arguments[1];", field, str(value))
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", field)

    def add_kpi(self, kpi, job_title, min_rating, max_rating, make_default=False):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()
        self.wait.until(EC.visibility_of_element_located(self.kpi_input)).send_keys(kpi)
        self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown)).click()
        self.wait.until(EC.visibility_of_element_located(self.job_title_option(job_title))).click()

        min_field = self.wait.until(EC.visibility_of_element_located(self.min_rating_input))
        self.clear_and_fill(min_field, min_rating)

        max_field = self.wait.until(EC.visibility_of_element_located(self.max_rating_input))
        self.clear_and_fill(max_field, max_rating)

        if make_default:
            switch = self.wait.until(EC.visibility_of_element_located(self.default_scale_switch))
            if not switch.is_selected():
                switch.click()
        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def assert_success(self):
        assert self.wait.until(EC.visibility_of_element_located(self.toast_message))
        time.sleep(3)

    # def select_job_title_search(self, job_title):
    #     # Click the Job Title dropdown
    #     dropdown = self.wait.until(EC.element_to_be_clickable((
    #         By.XPATH, "//label[contains(text(),'Job Title')]/following::div[contains(@class,'oxd-select-wrapper')]"
    #     )))
    #     dropdown.click()
    #     # Wait for the dropdown options to display and click the matching job title
    #     option = self.wait.until(EC.visibility_of_element_located((
    #         By.XPATH, f"//div[@role='listbox']//span[text()='{job_title}']"
    #     )))
    #
    #     # 4. Use JS to scroll the option into view in the dropdown panel
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", option)
    #
    #     # 5. Click the option
    #     option.click()
    #
    #     self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
    #
    #
    #
    #
    #
    # def verify_kpi_row_with_yes_state(self, kpi_name, job_title, expect_yes):
    #     self.driver.execute_script("window.scrollBy(0,400);")
    #     rows = self.driver.find_elements(By.XPATH,
    #                                      "//div[contains(@class, 'oxd-table-body')]/div[contains(@class, 'oxd-table-row')]")
    #     for row in rows:
    #         # Collect exact trimmed text for each cell
    #         cells = row.find_elements(By.XPATH, ".//div[contains(@class, 'oxd-table-cell')]")
    #         cell_texts = [cell.text.strip().lower() for cell in cells]
    #         kpi_match = kpi_name.strip().lower() in cell_texts
    #         role_match = job_title.strip().lower() in cell_texts
    #         has_yes = "yes" in cell_texts
    #         if kpi_match and role_match:
    #             if expect_yes and has_yes:
    #                 return True  # Only if "Yes" is there and expected
    #             if not expect_yes and not has_yes:
    #                 return True  # Only if "Yes" is not there and not expected
    #     return False
    #
    #
