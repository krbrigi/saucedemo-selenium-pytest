from utils.config import BASE_URL
from pages.LoginPage import LoginPage
from tests.testdata import LOGIN_SUCCESS_USERS, LOGIN_FAILED_USERS, PASSWORD
import pytest
import allure


@allure.feature("Login page")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("login page")
class TestLogin:
    @allure.story("Successful Login")
    @allure.title("Login with success user: {username}")
    @allure.tag("login")
    @pytest.mark.parametrize("username", LOGIN_SUCCESS_USERS)
    def test_login_successful(self, driver, logged_in, username):
        logged_in(username, PASSWORD)

        assert "inventory" in driver.current_url

    @allure.story("Failed Login")
    @allure.title("Login with invalid user: {username}")
    @allure.tag("login")
    @pytest.mark.parametrize("username, error", LOGIN_FAILED_USERS)
    def test_login_failed(self, driver, username, error):
        login_page = LoginPage(driver)
        login_page.open(BASE_URL)
        login_page.login(username, PASSWORD)

        assert login_page.get_error_message() == error

    @allure.story("Logout Flow")
    @allure.title("Logout from the page")
    @allure.tag("logout")
    def test_logout(self, driver, inventory_page):
        inventory_page.click_burger_menu()
        inventory_page.click_logout()

        assert driver.current_url == BASE_URL
