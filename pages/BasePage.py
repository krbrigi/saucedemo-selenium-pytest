from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
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

