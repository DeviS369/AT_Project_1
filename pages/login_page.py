from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        login_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        login_btn.click()

    def is_logged_in(self):
        # Dashboard presence indicates successful login
        try:
            dashboard = self.wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
            return dashboard.is_displayed()
        except:
            return False

    def get_error_message(self):
        error_list = self.wait.until(
            EC.visibility_of_any_elements_located((By.XPATH, "//div[contains(@class, 'oxd-alert-content')]//p"))
        )
        return error_list[0].text  # take the first element's text

