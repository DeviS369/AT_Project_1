import pytest
from selenium import webdriver
import time
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    time.sleep(5)
    driver.minimize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)
    request.cls.driver = driver
    yield driver
    driver.quit()
