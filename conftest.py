import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from utils.config import BASE_URL
from testdata import PASSWORD

@pytest.fixture()
def driver():
    options = Options()

    options.add_argument("--guest")
    options.add_argument("--lang=en")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture()
def logged_in(driver):
    def _login(username, password):
        login_page = LoginPage(driver)

        login_page.open(BASE_URL)
        login_page.login(username, password)

        return login_page

    return _login

@pytest.fixture()
def inventory_page(driver, logged_in):
    logged_in("standard_user", PASSWORD)

    return InventoryPage(driver)

@pytest.fixture()
def cart_with_product(inventory_page):
    def _add(product_id):
            inventory_page.add_product_to_cart(product_id)
            inventory_page.open_cart()
            return CartPage(inventory_page.driver)

    return _add