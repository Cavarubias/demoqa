from pages.base_page import BasePage
from components.components import WebElement



class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, "//*[contains(@id, 'delete-record')]", 'xpath')
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.registration_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.registration_form_first_name = WebElement(driver, '#firstName')
        self.registration_form_last_name = WebElement(driver, '#lastName')
        self.registration_form_email = WebElement(driver, '#userEmail')
        self.registration_form_age = WebElement(driver, '#age')
        self.registration_form_salary = WebElement(driver, '#salary')
        self.registration_form_department = WebElement(driver, '#department')
        self.registration_form_submit_btn = WebElement(driver, '#submit')
        self.added_row = WebElement(driver, "//*[contains(text(), 'Aleksey')]", 'xpath')
        self.btn_edit = WebElement(driver, "//*[contains(@id, 'edit-record')]", 'xpath')
        self.btn_rows_qty = WebElement(driver, 'div.-center > span.select-wrap.-pageSizeOptions > select')
        self.option_5_rows = WebElement(driver, 'div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_previous = WebElement(driver, 'div.-previous > button')
        self.total_pages_qty = WebElement(driver, 'span.-pageInfo > span')
        self.current_pages_qty = WebElement(driver, 'div.-center > span.-pageInfo > div > input[type=number]')
        self.column_title_first_name = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]', 'xpath')
        self.column_title_last_name = WebElement(driver,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[2]','xpath')
        self.column_title_age = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[3]', 'xpath')
        self.column_title_email = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[4]', 'xpath')
        self.column_title_salary = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[5]', 'xpath')
        self.column_title_department = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[6]', 'xpath')
        self.column_title_action = WebElement(driver, '//*[@id="app"]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[7]', 'xpath')