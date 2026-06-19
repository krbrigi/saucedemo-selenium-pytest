from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage


class CheckoutCompletePage(BasePage):
    BACK_HOME = (By.ID, "back-to-products")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-header")

    def click_back_home(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME)).click()

    def get_complete_message(self):
        complete_message = self.wait.until(
            EC.visibility_of_element_located(self.COMPLETE_TEXT)
        )
        return complete_message.text
