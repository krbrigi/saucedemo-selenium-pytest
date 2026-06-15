from testdata import LOGIN_SUCCESS_USERS, LOGIN_FAILED_USERS, PASSWORD
import pytest


class TestLogin:
    @pytest.mark.parametrize("username",  LOGIN_SUCCESS_USERS)
    def test_login_successful(self, driver, logged_in, username):
        logged_in(username, PASSWORD)

        assert "inventory" in driver.current_url

    @pytest.mark.parametrize("username", LOGIN_FAILED_USERS)
    def test_login_locked(self, driver, logged_in, username):
        logged_in(username, PASSWORD)
        assert "inventory" not in driver.current_url