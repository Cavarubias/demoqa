from pages.base_page import BasePage
from components.components import WebElement


class AccordionPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/accordian"
        super().__init__(driver, self.base_url)

        self.lorem_ipsum_text = WebElement(driver, '#section1Content > p')
        self.lorem_ipsum_title = WebElement(driver, '#section1Heading')
        self.where_does_it_come_from_text_first_paragraph = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.where_does_it_come_from_text_second_paragraph = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.why_do_we_use_it_text = WebElement(driver, '#section3Content > p')
