from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/"
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.button_element = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')


