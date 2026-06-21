from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage


class CheckoutOnePage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    ERROR_TEXT = (By.XPATH, "//div[@class='error-message-container error']/h3")

    def enter_first_name(self, firstname):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(lastname)

    def enter_postal_code(self, postalcode):
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(postalcode)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def click_cancel(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL)).click()

    def fill_checkout(self, firstname, lastname, postal_code):
        self.enter_first_name(firstname)
        self.enter_last_name(lastname)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_error_message(self):
        error_message =self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT))

        return error_message.text


