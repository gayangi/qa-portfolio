import time
from pages.login_page import LoginPage
from utils.driver_setup import get_driver

BASE_URL = "https://practicetestautomation.com/practice-test-login/"

def test_invalid_credentials_shows_error():
    driver = get_driver()
    login = LoginPage(driver)
    try:
        login.load(BASE_URL)
        login.enter_username("wrongUser")
        login.enter_password("wrongPass")
        login.click_login()
        time.sleep(1)
        error = login.get_error_text()
        assert error is not None and "invalid" in error.lower()
    finally:
        driver.quit()

def test_valid_credentials_logs_in():
    driver = get_driver()
    login = LoginPage(driver)
    try:
        login.load(BASE_URL)
        login.enter_username("student")
        login.enter_password("Password123")
        login.click_login()
        assert "Logged In Successfully" in driver.page_source or "logout" in driver.page_source.lower()
    finally:
        driver.quit()
