import pytest
import time
from utils.driver_factory import get_driver
from pages.login_page import LoginPage
from pages.pim_page import PimPage

@pytest.fixture
def logged_in_driver():
    driver = get_driver()
    login = LoginPage(driver)
    login.load("https://opensource-demo.orangehrmlive.com/")
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    yield driver
    driver.quit()

def test_add_employee(logged_in_driver):
    pim = PimPage(logged_in_driver)
    pim.navigate_to_pim()
    pim.add_employee("Test", "User")
    time.sleep(1)  # Give time for post-save UI update

def test_edit_employee(logged_in_driver):
    pim = PimPage(logged_in_driver)
    pim.navigate_to_pim()
    pim.add_employee("Test", "User")
    time.sleep(2)

    # Navigate back to the employee list page
    logged_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    pim.search_employee("Test User")
    pim.click_edit_employee("Test User")
    pim.update_last_name("Updated")
    time.sleep(2)


def test_delete_employee(logged_in_driver):
    pim = PimPage(logged_in_driver)
    pim.navigate_to_pim()
    #pim.add_employee("Test", "User")
    time.sleep(1)
     # Navigate back to the employee list page
    logged_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    #pim.search_employee1("Test User")
    pim.delete_employee("Test User")
    time.sleep(1)

    assert pim.is_employee_deleted("Test User")
