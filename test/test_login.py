import pytest
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.load("https://opensource-demo.orangehrmlive.com/")
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    assert login.is_logged_in()

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.load("https://opensource-demo.orangehrmlive.com/")
    login.enter_username("Admin")
    login.enter_password("WrongPassword")
    login.click_login()
    error_msg = login.get_error_message()
    assert "Invalid credentials" in error_msg
