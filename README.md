OrangeHRM Automation Framework
A production-quality UI test automation framework for the OrangeHRM web application, built using Python, Selenium, and Pytest. This project is a comprehensive solution designed for scalability, maintainability, and seamless integration into a CI/CD pipeline.

Highlights
Architected for Scale: Employs the Page Object Model (POM) to separate page locators and actions from test logic, making the suite highly maintainable and resilient to UI changes.

Data-Driven: All test data is externalized in JSON files and consumed via Pytest parametrization, allowing for easy test expansion and data management without code changes.

Enhanced Reporting: Features professional, interactive reporting with Allure Reports, including automatic screenshots on test failure to accelerate debugging.

CI/CD Ready: Structured for effortless execution in a CI environment like GitHub Actions.

Tech Stack
Language: Python 3.10+
Framework: Pytest
Web Automation: Selenium WebDriver
API Testing: Requests
Reporting: Allure Reports
Data: JSON
Dependency Management: requirements.txt

Repository Structure
.
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── (other page objects)
├── tests/
│   ├── test_login.py
│   └── (other test files)
├── data/
│   ├── test_data_login.json
│   └── (other data files)
├── utils/
│   ├── config.py
│   └── driver_factory.py
├── screenshots/
├── reports/
├── .gitignore
├── conftest.py
├── pytest.ini
└── requirements.txt

⚙️ Getting Started
1. Clone the Repository

git clone https://github.com/Rohith-SDET/OrangeHRM-Automation-Framework.git
cd OrangeHRM-Automation-Framework

2. Setup Virtual Environment
Create and activate a virtual environment to manage project dependencies.

Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
Install all necessary libraries using the requirements.txt file.
pip install -r requirements.txt

5. Run Tests
You can run the entire test suite or a specific test file.

Run all tests:

pytest -v
Run a specific module:
pytest tests/test_login.py

5. Generate Allure Report
Generate and view a professional, interactive Allure Report after your test run.

pytest --alluredir=allure-results
allure serve allure-results

Test Coverage
Module	- Scenarios
Login	- Valid and invalid login attempts with corresponding error message validation.
PIM	- Add a new employee and verify the creation via a search function.
Recruitment	- Create a new vacancy and validate the job title and hiring manager.
My Info	- Update employee details and confirm the changes are saved correctly.
Admin	- Filter user accounts by username, role, and status.

Engineering Principles
Encapsulation: The POM architecture encapsulates all page-specific logic, isolating test scripts from changes in the UI.

Hooks and Fixtures: Pytest fixtures are used to manage test lifecycle, including driver setup and teardown, while hooks automatically capture screenshots on failure, providing crucial debugging artifacts.

Test Data Separation: By storing data in JSON files, the test suite becomes more flexible and easier to maintain.

Configuration Management: The utils/config.py file allows for easy management of the base URL and other settings, enabling testing across different environments.
