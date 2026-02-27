import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage

@pytest.mark.ncheckout
@pytest.mark.parametrize("firstname, lastname, postalcode,expected_error",[
    ("","QA","12345","Error: First Name is required"),
    ("Louis", "","12345","Error: Last Name is required"),
    ("Louis", "QA", "","Error: Postal Code is required"),
])
def test_04_e2e_checkout_flow_negative (driver, firstname, lastname, postalcode,expected_error) :
     #Login
     login_page = LoginPage(driver)
     login_page.open()
     login_page.login("standard_user", "secret_sauce")
     
     #Add Product + Go To Cart
     product_page = ProductPage (driver)
     product_page.add_first_product_to_cart()
     product_page.go_to_cart()

     #Checkout
     checkout_page = CheckoutPage(driver)
     checkout_page.click_checkout()
     checkout_page.fill_checkout_info(firstname,lastname,postalcode)

     error_message = checkout_page.get_error_message()    
     assert expected_error in error_message

     #Save Screenshot Negative Case
     checkout_page.take_error_screenshot("checkout_negative")
    