from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from testdata import BACKPACK, USER_DATA
from utils.config import BASE_URL


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
