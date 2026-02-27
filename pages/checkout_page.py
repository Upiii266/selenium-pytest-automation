import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    CHECK_OUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    ZIP_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_TITLE = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")  # 👈 FIX locator

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_OUT_BUTTON)).click()

    def wait_for_checkout_info_page(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT))

    def _fill(self, locator, value):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(value)

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.wait_for_checkout_info_page()
        self._fill(self.FIRST_NAME_INPUT, first_name)
        self._fill(self.LAST_NAME_INPUT, last_name)
        self._fill(self.ZIP_INPUT, postal_code)
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()
        
    def wait_for_overview_page(self):
        self.wait.until(EC.url_contains("checkout-step-two.html"))
    
    def finish_checkout(self):
        self.wait_for_overview_page()
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()
        self.wait.until(EC.url_contains("checkout-complete.html"))
    
    def get_success_message(self):
        success = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TITLE))
        return success.text
    
    def get_error_message(self):
        error = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return error.text
    
    def take_error_screenshot(self,name_prefix) :
        screenshots_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name_prefix}_{timestamp}.png"

        self.driver.save_screenshot(os.path.join(screenshots_dir, filename))