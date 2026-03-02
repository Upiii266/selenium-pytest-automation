import pytest
import os
from selenium import webdriver
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture 
def driver(request):
    """Fixture utama untuk semua scenario default"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    _take_screenshot_if_failed(driver,request)
    driver.quit()

@pytest.fixture
def driver_for_remove(request):
    """Fixture khusus untuk scenario remove item"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/cart")
    yield driver
    _take_screenshot_if_failed(driver,request)
    driver.quit()

def _take_screenshot_if_failed(driver, request):
    """Function take screenshoot ketika negatif case & test failed"""
    rep_call = getattr(request.node, "rep_call", None)
    rep_setup = getattr(request.node, "rep_setup", None)
    rep_teardown = getattr(request.node,"rep_teardown",None)

    if any ([rep_call and rep_call.failed, rep_setup and rep_setup.failed, rep_teardown and rep_teardown.failed]):
        screenshots_dir = os.path.join(BASE_DIR, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_name = request.node.name.replace("[", "_").replace("]", "_")
        filename = f"{safe_name}_failed_{timestamp}.png"

        try:
            driver.save_screenshot(os.path.join(screenshots_dir, filename))
            print(f"\n📸 Screenshot saved to: {filename}")
        except Exception as e:
            print(f"⚠️ Failed to take screenshot: {e}")

