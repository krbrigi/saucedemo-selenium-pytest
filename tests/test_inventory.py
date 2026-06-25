from testdata import BACKPACK, BIKE_LIGHT


class TestInventory:
    def test_add_product_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 0

    def test_add_two_products_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 2

    def test_remove_one_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 1

    def test_remove_all_products_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 0

    def test_sort_name_az(self, inventory_page):
        inventory_page.select_sorting("az")
        names = inventory_page.get_items_names()

        assert names == sorted(names)

    def test_sort_name_za(self, inventory_page):
        inventory_page.select_sorting("za")
        names = inventory_page.get_items_names()

        assert names == sorted(names, reverse=True)

    def test_sort_price_low_high(self, inventory_page):
        inventory_page.select_sorting("lohi")
        item_prices = inventory_page.get_items_prices()
        prices = [float(price[1:]) for price in item_prices]

        assert prices == sorted(prices)

    def test_sort_price_high_low(self, inventory_page):
        inventory_page.select_sorting("hilo")
        item_prices = inventory_page.get_items_prices()
        prices = [float(price[1:]) for price in item_prices]

        assert prices == sorted(prices, reverse=True)

