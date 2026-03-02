import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
import time

@pytest.mark.remove1
def test_05_e2e_remove_product_flow (driver) :
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user","secret_sauce")

    product_page.add_first_product_to_cart()
    product_page.add_second_product_to_cart()

    #stepremovesecondproduct
    product_page.remove_second_product_from_cart()
    time.sleep(5) #jedalihatitemterhapus

    #gotocarcheck
    product_page.go_to_cart()
    
    