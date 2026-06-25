from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage
from testdata import BACKPACK, USER_DATA
import allure


@allure.feature("End to end")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("e2e")
class TestE2E:
    @allure.story("Successful Purchase Flow")
    @allure.title("Complete a full product purchase from cart to order confirmation")
    @allure.tag("valid")
    def test_checkout_complete(self, driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        checkout_one_page = CheckoutOnePage(driver)

        cart_page.checkout()
        checkout_one_page.fill_checkout(
            USER_DATA["first_name"],
            USER_DATA["last_name"],
            USER_DATA["postal_code"]
        )

        checkout_two_page = CheckoutTwoPage(driver)

        assert BACKPACK["name"] in checkout_two_page.get_item_names()

        checkout_two_page.click_finish()
        checkout_complete_page = CheckoutCompletePage(driver)

        assert checkout_complete_page.get_complete_message() == "Thank you for your order!"
