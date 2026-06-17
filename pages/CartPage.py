from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage


class CartPage(BasePage):
    CONTINUE = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT = (By.ID, "logout_sidebar_link")

    def remove_product_from_cart(self, product_id):
        locator = (By.ID, f"remove-{product_id}")

        remove_button = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        remove_button.click()

    def continue_shopping(self):
        button_continue = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE)
        )

        button_continue.click()


    def checkout(self):
        button_checkout = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT)
        )

        button_checkout.click()

    def get_cart_badge_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        if not badges:
            return 0

        return int(badges[0].text)

