OrangeHRM UI Automation Suite
Production-style UI automation for the OrangeHRM demo app using Python, Selenium, Pytest, and Page Object Model (POM). The suite is data-driven, report-rich, and CI/CD ready for fast, repeatable runs.

Highlights
Page Object Model for clean locators and reusable actions across modules.

JSON-driven test data with Pytest parametrization.

Failure screenshots auto-captured and attached to reports.

Single-command execution and CI-friendly structure.

Tech Stack
Python 3.10+

Selenium WebDriver

Pytest (fixtures, hooks, parametrization)

Reporting: pytest-html, Allure (optional)

Data: JSON

Repository Structure
pages/ — Page Objects: login, pim, leave, recruitment, performance, my_info, time_attendance, admin.

tests/ — Test modules mapping to features (e.g., test_login.py, test_pim.py).

data/ — Test datasets (login, pim, recruitment, performance, my_info, admin).

utils/ — driver_factory.py, config.py, shared data (test_data_inputs.json).

screenshots/ — Failure images saved by pytest hook.

reports/ and allure-results/ — HTML and Allure outputs.

Test Matrix (plain text)
Login: valid and invalid login with message validation (data/test_data_login.json).

PIM: add employee and search by name/ID (data/test_data_pim.json).

Leave: open Apply page and validate “No Leave Types with Leave Balance” (N/A).

Recruitment: add vacancy (job title, hiring manager, positions) (data/recruitement_test_data.json).

Performance: add KPI, rating bounds, default toggle (data/performance_test_data.json).

My Info: update profile fields (IDs, DOB, gender) and verify success toast (data/my_info_test_data.json).

Time & Attendance: navigate to Timesheet and verify page content (N/A).

Admin: filter users by username/role/status/employee and list results (data/tes_data_admin.json).

Setup
Create and activate virtual environment

Windows:

text
python -m venv .venv
.venv\Scripts\activate
macOS/Linux:

text
python -m venv .venv
source .venv/bin/activate
Install dependencies

text
pip install -r requirements.txt
Or install core packages:

text
pip install selenium pytest pytest-html allure-pytest python-dotenv
Optional: set BASE_URL

Default is in utils/config.py. To override:

Windows:

text
set BASE_URL=https://your-env-url
macOS/Linux:

text
export BASE_URL=https://your-env-url
Running Tests
Run all tests (HTML + Allure paths can be set in pytest.ini):

text
pytest -v
Run a specific module:

text
pytest tests/test_pim.py
Generate standalone HTML report:

text
pytest --html=reports/report.html --self-contained-html
Generate and view Allure:

text
pytest --alluredir=allure-results
allure serve allure-results
Reporting & Artifacts
HTML report: reports/report.html (failure screenshots embedded when plugin is present).

Allure: allure-results/ with steps and screenshots for failed steps (use allure serve to view).

Raw screenshots: screenshots/ captured via pytest hook on failures.

What’s Engineered
POM encapsulation to isolate selectors/actions and reduce flakiness.

JSON-driven parametrization for scalable coverage.

Pytest hooks in conftest.py to auto-attach failure screenshots.

Configurable environments via utils/config.py and environment variables.

CI/CD Ready
Typical pipeline steps:

Set up Python

pip install -r requirements.txt

pytest -v --alluredir=allure-results

Upload reports/, allure-results/, and screenshots/ as build artifacts
