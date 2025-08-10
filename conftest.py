import pytest
<<<<<<< HEAD
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
=======
import os
import shutil
import datetime
from utils.driver_factory import get_driver
from utils.config import get_base_url


# ✅ Step 1: Clean screenshots/ before run
def pytest_sessionstart(session):
    screenshots_dir = "screenshots"
    try:
        shutil.rmtree(screenshots_dir)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f" Could not clean screenshots folder: {e}")


# ✅ Step 2: Driver fixture (keep this)
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(get_base_url())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


# ✅ Step 3: Screenshot on every test and attach to Allure/HTML
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get("driver", None)

    if driver is None or not rep.when == "call":
        return

    # Save screenshot
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_name = item.name.replace("/", "_").replace("[", "").replace("]", "")
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{rep.outcome}_{timestamp}.png")

    driver.save_screenshot(screenshot_path)
    print(f"\n📸 Screenshot saved: {screenshot_path}")

    # Attach to Allure
    try:
        import allure
        with open(screenshot_path, "rb") as f:
            allure.attach(f.read(), name=test_name, attachment_type=allure.attachment_type.PNG)
    except ImportError:
        pass

    # Attach to pytest-html report
    if item.config.pluginmanager.hasplugin("html"):
        extra = getattr(rep, "extra", [])
        html = f'<div><img src="{screenshot_path}" alt="screenshot" ' \
               f'style="width:600px" onclick="window.open(this.src)" /></div>'
        try:
            import pytest_html
            extra.append(pytest_html.extras.html(html))
        except ImportError:
            pass
        rep.extra = extra
>>>>>>> e0eb84e (Initial commit)
