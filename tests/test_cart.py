from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from testdata import PASSWORD

class TestCart():
    def test_remove_product_from_cart(self,driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.open_cart()
        cart_page.remove_product_from_cart("sauce-labs-backpack")

        assert cart_page.get_cart_badge_count() == 0

    def test_continue_shopping(self, driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        inventory_page.open_cart()
        cart_page.continue_shopping()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

