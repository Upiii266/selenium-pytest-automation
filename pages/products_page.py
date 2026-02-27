from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage :
    ADD_FIRST_PRODUCT = (By.CSS_SELECTOR,".inventory_item:first-child button")
    CART_ICON = (By.ID,"shopping_cart_container")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)
    
    def add_first_product_to_cart(self) :
        self.wait.until(EC.element_to_be_clickable(self.ADD_FIRST_PRODUCT)).click()

    def go_to_cart(self) :
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()