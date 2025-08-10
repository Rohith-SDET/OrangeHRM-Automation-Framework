# tests/test_time_attendance.py

import pytest
from pages.login_page import LoginPage
from pages.time_attendance_page import TimeAttendancePage

def test_view_timesheet(driver):
    """Test to view timesheet in Time & Attendance module."""

    # ✅ Login (URL is already opened by driver fixture from conftest.py)
    login = LoginPage(driver)
    login.login("Admin", "admin123")  # You can swap with test data fixture

    # ✅ Navigate and perform actions
    time_page = TimeAttendancePage(driver)
    time_page.navigate_to_time_module()
    time_page.navigate_to_timesheet_tab()
    time_page.verify_timesheet_page()


    # ✅ Assertion
    assert "Timesheet" in driver.page_source
