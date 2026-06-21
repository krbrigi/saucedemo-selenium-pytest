from testdata import BACKPACK, BIKE_LIGHT


class TestInventory:
    def test_add_product_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 0

    def test_add_two_product_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 2

    def test_remove_one_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_all_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 0


