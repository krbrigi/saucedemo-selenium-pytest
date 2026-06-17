import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.LoginPage import LoginPage
from utils.config import BASE_URL

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
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)

    def _login(username, password):
        login_page.login(username, password)
        return login_page

    return _login

