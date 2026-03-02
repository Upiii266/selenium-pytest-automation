from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class ProductPage :
    ADD_FIRST_PRODUCT = (By.ID,"add-to-cart-sauce-labs-backpack")
    ADD_SECOND_PRODUCT = (By.ID,"add-to-cart-sauce-labs-bike-light")
    REMOVE_SECOND_PRODUCT = (By.ID,"remove-sauce-labs-bike-light")
    CART_ICON = (By.ID,"shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME,"shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)
    
    def add_first_product_to_cart(self) :
        self.wait.until(EC.element_to_be_clickable(self.ADD_FIRST_PRODUCT)).click()

    #add2nditem
    def add_second_product_to_cart (self) :
        self.wait.until(EC.element_to_be_clickable(self.ADD_SECOND_PRODUCT)).click()
    
    #remove2nditem
    def remove_second_product_from_cart  (self) :
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_SECOND_PRODUCT)).click()

    def go_to_cart(self) :
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()
    
    def get_cart_count (self) :
        try :
            badge = self.driver.find_element(*self.CART_BADGE)
            return int(badge.text)
        except NoSuchElementException :
            return 0