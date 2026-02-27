import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID,"login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login (self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    
    def get_error_message(self):
        el = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located
            ((By.CSS_SELECTOR,"[data-test='error']")))
        return el.text
    
    def  is_error_visible(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR,"[data-test='error']")) > 0
    
    def take_error_screenshot(self,name_prefix) :
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name_prefix}_{timestamp}.png"

        self.driver.save_screenshot(os.path.join(screenshots_dir, filename))