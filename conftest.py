import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from utils.config import BASE_URL

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture()
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)

    def _login(username, password):
        login_page.login(username, password)
        return login_page

    return _login

