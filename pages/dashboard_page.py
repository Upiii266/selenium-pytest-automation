from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage :
    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self) :
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_list")))
        return True
    
    
    
    def get_title(self):
        return self.driver.find_element(By.CLASS_NAME,"title").text
    
