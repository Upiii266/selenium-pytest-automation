import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.pcheckout
def test_03_e2e_checkout_flow (driver) :
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user","secret_sauce")

    product_page.add_first_product_to_cart()
    product_page.go_to_cart()

    checkout_page.click_checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert checkout_page.get_success_message() == "Thank you for your order!"