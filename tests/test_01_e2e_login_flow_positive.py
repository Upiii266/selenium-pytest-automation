import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

@pytest.mark.plogin
def test_login_to_dashboard(driver):
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage (driver)

    login_page.open()
    login_page.login("standard_user","secret_sauce")

    assert dashboard_page.is_loaded()
    assert dashboard_page.get_title() == "Products"