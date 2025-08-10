import pytest
import json
import os
import shutil
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver_factory import get_driver
from utils.config import get_base_url

@pytest.fixture(scope="session")
def load_test_data():
    with open("utils/test_data_inputs.json") as f:
        return json.load(f)["testcases"]

def pytest_sessionstart():
    folder = "screenshots"
    if os.path.exists(folder):
        try:
            shutil.rmtree(folder)
        except Exception as e:
            print(f"Failed to clean screenshots: {e}")


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    driver.get(get_base_url())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    driver_obj = item.funcargs.get("driver", None)
    # Take a screenshot ONLY if test fails (when="call" phase)
    if driver_obj and rep.when == "call" and rep.failed:
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name = item.name.replace("/", "_").replace("[", "").replace("]", "")
        os.makedirs("screenshots", exist_ok=True)
        path = os.path.join("screenshots", f"{name}_{ts}.png")
        driver_obj.save_screenshot(path)
        print(f"\n📸 Screenshot saved: {path}")
        try:
            import allure
            with open(path, "rb") as f:
                allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)
        except ImportError:
            pass
        if item.config.pluginmanager.hasplugin("html"):
            extra = getattr(rep, "extra", [])
            html = f'<div><img src="{path}" alt="screenshot" style="width:600px" onclick="window.open(this.src)"/></div>'
            try:
                import pytest_html
                extra.append(pytest_html.extras.html(html))
            except ImportError:
                pass
            rep.extra = extra
