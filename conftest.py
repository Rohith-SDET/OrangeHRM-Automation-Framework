import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

URL = "https://opensource-demo.orangehrmlive.com/"

@pytest.fixture(scope="session")
def load_test_data():
    with open("utils/test_data_inputs.json") as file:
        return json.load(file)["testcases"]

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
    driver.get(URL)
    yield driver
    driver.quit()
