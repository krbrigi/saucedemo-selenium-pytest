from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.BasePage import BasePage


class InventoryPage(BasePage):
    SORT = (By.CLASS_NAME, "product_sort_container")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")
    ITEMS_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEMS_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def select_sorting(self, sorting_value):
        select_object = Select(
            self.wait.until(
                EC.visibility_of_element_located(self.SORT)
            )
        )

        select_object.select_by_value(sorting_value)

    def add_product_to_cart(self, product_id):
        locator = (By.ID, f"add-to-cart-{product_id}")

        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        add_to_cart_button.click()

    def remove_product_from_cart(self, product_id):
        locator = (By.ID, f"remove-{product_id}")

        remove_button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        remove_button.click()

    def open_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable(self.CART))

        cart.click()

    def get_cart_badge_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0

        return int(badges[0].text)

    def click_burger_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.BURGER_MENU)).click()

    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT)).click()

    def get_items_names(self):
        self.wait.until(
            EC.presence_of_element_located(self.ITEMS_NAME)
        )
        items = self.driver.find_elements(*self.ITEMS_NAME)
        product_names = [item.text for item in items]

        return product_names

    def get_items_prices(self):
        self.wait.until(
            EC.presence_of_element_located(self.ITEMS_PRICE)
        )
        items = self.driver.find_elements(*self.ITEMS_PRICE)
        product_prices = [item.text for item in items]

        return product_prices
