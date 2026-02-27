import pytest
from pages.login_page import LoginPage

@pytest.mark.nlogin
@pytest.mark.parametrize ("username, password, expected_error",[
    ("standard_user","wrong_pass","Epic sadface: Username and password do not match any user in this service"),
    ("","secret_sauce","Epic sadface: Username is required"),
    ("standard_user","","Epic sadface: Password is required"),
    ("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out."),
])
def test_02_e2e_login_flow_negative_cases (driver,username,password,expected_error) :
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username,password)

    error_message = login_page.get_error_message()
    assert expected_error in error_message

    #Save Screenshot Negative Case
    login_page.take_error_screenshot("login_negative")