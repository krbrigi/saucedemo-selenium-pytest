from testdata import BACKPACK

class TestCart():
    def test_remove_product_from_cart(self, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        cart_page.remove_product_from_cart(BACKPACK["id"])

        assert cart_page.get_cart_badge_count() == 0

    def test_continue_shopping(self,driver, cart_with_product):
        cart_page = cart_with_product(BACKPACK["id"])
        cart_page.continue_shopping()

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"

