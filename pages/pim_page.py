from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def navigate_to_pim(self):
        """Navigate to the PIM section"""
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()

    def click_add_employee(self):
        """Click the Add Employee button"""
        add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add')]")))
        add_btn.click()

    def add_employee(self, first_name, last_name):
        """Add a new employee"""
        self.click_add_employee()
        fn_input = self.wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        ln_input = self.driver.find_element(By.NAME, "lastName")
        fn_input.clear()
        fn_input.send_keys(first_name)
        ln_input.clear()
        ln_input.send_keys(last_name)
        save_btn = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")
        self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.3);", save_btn)
        save_btn.click()

    def search_employee(self, name):
        try:
            emp_name_input = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Type for hints...']")  # fallback here if needed
            ))
            emp_name_input.clear()
            emp_name_input.send_keys(name)

            search_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
            ))
            search_btn.click()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", search_btn)
        except TimeoutException:
            raise Exception("Failed to find employee name input field for search.")
        
    def search_employee1(self, name):
        try:
            emp_name_input = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//input[@placeholder='Type for hints...']")  # fallback here if needed
            ))
            emp_name_input.clear()
            emp_name_input.send_keys(name)

            search_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
            ))
            search_btn.click()
            self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.3);", search_btn)
        except TimeoutException:
            raise Exception("Failed to find employee name input field for search.")

    def click_edit_employee(self, name):
        """Click the edit button on the search results"""
        self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@role='rowgroup']//div[@role='row']")))
        edit_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]")))
        edit_btn.click()

    def update_last_name(self, new_last_name):
        """Update the employee's last name, scroll into view if needed."""
        ln_input = self.wait.until(EC.presence_of_element_located(
            (By.NAME, "lastName")
        ))
        ln_input.clear()
        ln_input.send_keys(new_last_name)
        save_btn = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button")
        save_btn.click()                             

    def delete_employee(self, name): 
        """Delete the employee from the list"""
        self.search_employee1(name)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='rowgroup']//input[@type='checkbox']"))).click()
        delete_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Delete Selected')]")))
        delete_button.click()
        confirm_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Yes, Delete')]")))
        confirm_button.click()

    def is_employee_deleted(self, name):
        """Check if the employee was successfully deleted"""
        self.search_employee(name)
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='No Records Found']")))
            return True
        except:
            return False
