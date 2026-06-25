from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    ERROR_TEXT = (By.XPATH, "//div[@class='error-message-container error']/h3")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self, url):
        self.driver.get(url)


    def get_current_url(self):
        return self.driver.current_url

    def save_screenshot_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.driver.save_screenshot(f"screenshot_{timestamp}.png")

    def get_error_message(self):
        error_message =self.wait.until(EC.visibility_of_element_located(self.ERROR_TEXT))
        return error_message.text