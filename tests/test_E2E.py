from pages.CheckoutOnePage import CheckoutOnePage
from pages.CheckoutTwoPage import CheckoutTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from testdata import PASSWORD

class TestE2E:
    def test_checkout_complete(self, driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_one_page = CheckoutOnePage(driver)
        checkout_two_page = CheckoutTwoPage(driver)
        checkout_complete_page = CheckoutCompletePage(driver)

        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.open_cart()
        cart_page.checkout()
        checkout_one_page.fill_checkout("Elek", "Test", "1111")

        assert "Sauce Labs Backpack" in checkout_two_page.get_item_names()

        checkout_two_page.click_finish()

        assert checkout_complete_page.get_complete_message() == "Thank you for your order!"