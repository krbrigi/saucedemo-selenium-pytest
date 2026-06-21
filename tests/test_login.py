from config import BASE_URL
from testdata import LOGIN_SUCCESS_USERS, LOGIN_FAILED_USERS, PASSWORD
import pytest


class TestLogin:
    @pytest.mark.parametrize("username", LOGIN_SUCCESS_USERS)
    def test_login_successful(self, driver, logged_in, username):
        logged_in(username, PASSWORD)

        assert "inventory" in driver.current_url

    @pytest.mark.parametrize("username", LOGIN_FAILED_USERS)
    def test_login_locked(self, driver, logged_in, username):
        logged_in(username, PASSWORD)

        assert "inventory" not in driver.current_url

    def test_logout(self, driver, inventory_page):
        inventory_page.click_burger_menu()
        inventory_page.click_logout()

        assert driver.current_url == BASE_URL
