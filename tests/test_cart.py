from testdata import BACKPACK
from utils.config import BASE_URL
import allure


@allure.feature("Cart")
@allure.severity(allure.severity_level.CRITICAL)
class TestCart:
    @allure.story("Removing Items")
    @allure.title("Remove a product from the cart on the cart page")
    @allure.tag("remove")
    def test_remove_product_from_cart(self, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        cart_page.remove_product_from_cart(BACKPACK["id"])

        assert cart_page.get_cart_badge_count() == 0

    @allure.story("Navigation Flow")
    @allure.title("Return to inventory page using 'Continue Shopping' button")
    @allure.tag("navigation")
    def test_continue_shopping(self,driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        cart_page.continue_shopping()

        assert driver.current_url == f"{BASE_URL}inventory.html"

    @allure.story("Navigation Flow")
    @allure.title("Navigate to checkout page using 'Checkout' button")
    @allure.tag("navigation")
    def test_navigate_to_checkout(self, driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        cart_page.checkout()

        assert driver.current_url == f"{BASE_URL}checkout-step-one.html"

