from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from testdata import PASSWORD, BACKPACK

class TestCheckout:
    def test_checkout_fill_info(self, driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_one_page = CheckoutOnePage(driver)

        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.open_cart()
        cart_page.checkout()
        checkout_one_page.fill_checkout("Elek", "Test", "1111")

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    def test_checkout_item_in_cart(self, driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_one_page = CheckoutOnePage(driver)
        checkout_two_page = CheckoutTwoPage(driver)

        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.open_cart()
        cart_page.checkout()
        checkout_one_page.fill_checkout("Elek", "Test", "1111")

        assert BACKPACK["name"] in checkout_two_page.get_item_names()


