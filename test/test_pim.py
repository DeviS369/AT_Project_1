import pytest
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
    
def test_edit_employee(logged_in_driver):
    pim = PimPage(logged_in_driver)
    pim.navigate_to_pim()
    pim.add_employee("Test", "User")
   
    logged_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    pim.search_employee("Test User")
    pim.click_edit_employee("Test User")
    pim.update_last_name("Updated")
   
def test_delete_employee(logged_in_driver):
    pim = PimPage(logged_in_driver)
    pim.navigate_to_pim()
    logged_in_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    pim.delete_employee("Test User")
    time.sleep(1)
    assert pim.is_employee_deleted("Test User")
