from testdata import BACKPACK, BIKE_LIGHT
import allure


@allure.feature("Inventory")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("inventory")
class TestInventory:
    @allure.story("Cart Operations")
    @allure.title("Add a product to the cart")
    @allure.tag("add")
    def test_add_product_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 1

    @allure.story("Cart Operations")
    @allure.title("Remove the product from the cart")
    @allure.tag("remove")
    def test_remove_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])

        assert inventory_page.get_cart_badge_count() == 0

    @allure.story("Cart Operations")
    @allure.title("Add two products to the cart")
    @allure.tag("add")
    def test_add_two_products_to_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 2

    @allure.story("Cart Operations")
    @allure.title("Remove just one product from the cart")
    @allure.tag("remove")
    def test_remove_one_product_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 1

    @allure.story("Cart Operations")
    @allure.title("Remove all products from the cart")
    @allure.tag("remove")
    def test_remove_all_products_from_cart(self, inventory_page):
        inventory_page.add_product_to_cart(BACKPACK["id"])
        inventory_page.add_product_to_cart(BIKE_LIGHT["id"])
        inventory_page.remove_product_from_cart(BACKPACK["id"])
        inventory_page.remove_product_from_cart(BIKE_LIGHT["id"])

        assert inventory_page.get_cart_badge_count() == 0

    @allure.story("Product Sorting")
    @allure.title("Sort products by name A-Z")
    @allure.tag("sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_name_az(self, inventory_page):
        inventory_page.select_sorting("az")
        names = inventory_page.get_items_names()

        assert names == sorted(names)

    @allure.story("Product Sorting")
    @allure.title("Sort products by name Z-A")
    @allure.tag("sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_name_za(self, inventory_page):
        inventory_page.select_sorting("za")
        names = inventory_page.get_items_names()

        assert names == sorted(names, reverse=True)

    @allure.story("Product Sorting")
    @allure.title("Sort products by price low to high")
    @allure.tag("sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_price_low_high(self, inventory_page):
        inventory_page.select_sorting("lohi")
        item_prices = inventory_page.get_items_prices()
        prices = [float(price[1:]) for price in item_prices]

        assert prices == sorted(prices)

    @allure.story("Product Sorting")
    @allure.title("Sort products by price high to low")
    @allure.tag("sorting")
    @allure.severity(allure.severity_level.NORMAL)
    def test_sort_price_high_low(self, inventory_page):
        inventory_page.select_sorting("hilo")
        item_prices = inventory_page.get_items_prices()
        prices = [float(price[1:]) for price in item_prices]

        assert prices == sorted(prices, reverse=True)
