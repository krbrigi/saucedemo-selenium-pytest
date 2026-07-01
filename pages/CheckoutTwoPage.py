from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage


class CheckoutTwoPage(BasePage):
    CANCEL = (By.ID, "cancel")
    FINISH = (By.ID, "finish")
    ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        self.wait.until(
            EC.presence_of_element_located(self.ITEMS)
        )
        items = self.driver.find_elements(*self.ITEMS)
        product_names = [item.text for item in items]

        return product_names

    def click_cancel(self):
        cancel_button = self.wait.until(
            EC.element_to_be_clickable(self.CANCEL)
        )

        cancel_button.click()

    def click_finish(self):
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.FINISH)
        )

        finish_button.click()
