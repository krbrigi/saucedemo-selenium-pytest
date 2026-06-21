from testdata import BACKPACK


class TestInventory:
    def test_add_product_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 0

