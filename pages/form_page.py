from pages.base_page import BasePage
from components.components import WebElement



class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/automation-practice-form"
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies_checkbox_1 = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.student_registration_form = WebElement(driver, '#userForm')
        self.state_dropdown = WebElement(driver, '#state > div')
        self.state_dropdown_ncr = WebElement(driver, '#react-select-3-option-0')
        self.city_dropdown = WebElement(driver, '#city')
        self.city_dropdown_agra = WebElement(driver, '#react-select-4-option-0')