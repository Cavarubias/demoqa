from pages.form_page import FormPage
import time

def test_form_page(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9992223344')
    form_page.hobbies_checkbox_1.click_force()
    form_page.current_address.send_keys('Saint-Petersburg, Nevsky pr., 1')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

def test_state_and_city_dropdowns(browser):
    form_page = FormPage(browser)

    form_page.visit()
    form_page.state_dropdown.click()
    time.sleep(2)
    form_page.state_dropdown_ncr.click()
    time.sleep(2)
    form_page.city_dropdown.click()
    time.sleep(2)
    form_page.city_dropdown_agra.click()


#setTimeout (() => {debugger;},3000) - JS-код останавливает изменение html в браузере

