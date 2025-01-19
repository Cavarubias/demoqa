from pages.base_page import BasePage
from components.components import WebElement



class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/modal-dialogs"
        super().__init__(driver, self.base_url)

        self.menu_buttons = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul')
        self.main_page_icon = WebElement(driver,'#app > header > a')