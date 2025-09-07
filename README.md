# OrangeHRM Automation Framework

## About OrangeHRM
OrangeHRM is a popular open-source Human Resource Management (HRM) web application used to manage employee information, leave, recruitment, performance, and time & attendance.  
This project automates its UI using Python, Selenium, and Pytest to demonstrate enterprise-grade automation practices.
This project is designed for **scalability, maintainability, and seamless CI/CD integration**, making it portfolio-ready for SDET and QA automation roles.

---

## 🚀 Highlights

- **Architected for Scale**:  
  Uses the **Page Object Model (POM)** to separate locators and actions from test logic, ensuring resilience to UI changes.  

- **Data-Driven Testing**:  
  Test data is externalized in **JSON files** and consumed via **Pytest parametrization** for flexible, scalable scenarios.  

- **Enhanced Reporting**:  
  Integrated with **Allure Reports** and **failure screenshot capture** to accelerate debugging and provide professional reporting.  

- **CI/CD Ready**:  
  Structured for smooth execution in pipelines (e.g., **GitHub Actions**, **Jenkins**) with reports and artifacts auto-generated.  

---

## 🛠 Tech Stack

| Category             | Tools / Frameworks              |
|----------------------|----------------------------------|
| Language             | Python 3.10+                    |
| Test Framework       | Pytest                          |
| Web Automation       | Selenium WebDriver              |
| API Testing (optional)| Requests                       |
| Reporting            | Allure Reports, pytest-html     |
| Data                 | JSON                            |
| Dependency Mgmt      | requirements.txt                |

---

## ⚙️ Getting Started

### 1. Clone the Repository
bash
git clone https://github.com/Rohith-SDET/OrangeHRM-Automation-Framework.git
cd OrangeHRM-Automation-Framework

2. Setup Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


macOS/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies:
pip install -r requirements.txt

4. Run Tests

Run all tests:
pytest -v


Run a specific module:
pytest tests/test_login.py

5. Generate Allure Report
pytest --alluredir=allure-results
allure serve allure-results

Test Coverage:

| Module          | Scenarios                                                    |
| --------------- | ------------------------------------------------------------ |
| **Login**       | Valid & invalid login attempts with error message validation |
| **PIM**         | Add a new employee and verify via search                     |
| **Recruitment** | Create vacancy, validate job title & hiring manager          |
| **My Info**     | Update employee details & confirm persistence                |
| **Admin**       | Filter user accounts by username, role, and status           |

Engineering Principles:

Encapsulation → POM isolates page logic, reducing flakiness & maintenance overhead.

Fixtures & Hooks → Pytest fixtures manage driver setup/teardown, hooks auto-capture screenshots.

Test Data Separation → JSON files externalize test data for flexibility and maintainability.

Config Management → utils/config.py enables environment-based execution (staging, prod, etc.).


CI/CD Ready:

Easily integrated with GitHub Actions or Jenkins. Typical pipeline steps:

Setup Python

Install dependencies

Run tests with pytest

Collect Allure/HTML reports + screenshots as build artifacts


