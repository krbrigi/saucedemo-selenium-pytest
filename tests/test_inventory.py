from pages.InventoryPage import InventoryPage
from testdata import PASSWORD

class TestInventory:
    def test_add_product_to_cart(self,driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-backpack")

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_product_from_cart(self,driver, logged_in):
        logged_in("standard_user", PASSWORD)
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-backpack")
        inventory_page.remove_product_from_cart("sauce-labs-backpack")

        assert inventory_page.get_cart_badge_count() == 0

