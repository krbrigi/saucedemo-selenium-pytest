from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage
from testdata import BACKPACK, USER_DATA


class TestE2E:
    def test_checkout_complete(self, driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        checkout_one_page = CheckoutOnePage(driver)
        checkout_two_page = CheckoutTwoPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        cart_page.checkout()
        checkout_one_page.fill_checkout(
            USER_DATA["first_name"],
            USER_DATA["last_name"],
            USER_DATA["postal_code"]
        )

        assert BACKPACK["name"] in checkout_two_page.get_item_names()

        checkout_two_page.click_finish()

        assert checkout_complete_page.get_complete_message() == "Thank you for your order!"
