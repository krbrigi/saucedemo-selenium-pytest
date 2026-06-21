from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from testdata import BACKPACK, USER_DATA, CHECKOUT_NEGATIVE_CASES
from utils.config import BASE_URL
import pytest


class TestCheckout:
    def test_checkout_fill_info(self, driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        checkout_one_page = CheckoutOnePage(driver)

        cart_page.checkout()
        checkout_one_page.fill_checkout(
            USER_DATA["first_name"],
            USER_DATA["last_name"],
            USER_DATA["postal_code"]
        )

        assert driver.current_url == f"{BASE_URL}checkout-step-two.html"

    @pytest.mark.parametrize("first_name, last_name, postal_code, error", CHECKOUT_NEGATIVE_CASES)
    def test_checkout_fill_failed(self, driver, cart_with_product, first_name, last_name, postal_code, error):
        cart_page = cart_with_product(BACKPACK["id"])
        checkout_one_page = CheckoutOnePage(driver)

        cart_page.checkout()
        checkout_one_page.fill_checkout(
            first_name,
            last_name,
            postal_code
        )

        assert checkout_one_page.get_error_message() == error

    def test_checkout_item_in_cart(self, driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        checkout_one_page = CheckoutOnePage(driver)
        checkout_two_page = CheckoutTwoPage(driver)

        cart_page.checkout()
        checkout_one_page.fill_checkout(
            USER_DATA["first_name"],
            USER_DATA["last_name"],
            USER_DATA["postal_code"]
        )

        assert BACKPACK["name"] in checkout_two_page.get_item_names()
