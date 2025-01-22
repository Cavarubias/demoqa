from pages.tables import Tables
#import allure
import time

def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(2)
    assert page_tables.no_data.exist

def test_table_add_and_edit(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.registration_form.exist()
    page_tables.registration_form_submit_btn.click()
    assert page_tables.registration_form.exist()
    page_tables.registration_form_first_name.send_keys('Aleksey')
    page_tables.registration_form_last_name.send_keys('Grebeshkov')
    page_tables.registration_form_email.send_keys('grebeshkov@gmail.com')
    page_tables.registration_form_age.send_keys('35')
    page_tables.registration_form_salary.send_keys('25000')
    page_tables.registration_form_department.send_keys('BUH')
    page_tables.registration_form_submit_btn.click()
    time.sleep(2)

    assert page_tables.added_row.exist()
    page_tables.btn_edit.click()
    time.sleep(2)
    assert page_tables.registration_form.exist()
    assert page_tables.registration_form_first_name.get_dom_attribute('value') == 'Aleksey'
    page_tables.registration_form_first_name.clear()
    time.sleep(2)
    page_tables.registration_form_first_name.send_keys('Not Aleksey')
    page_tables.registration_form_submit_btn.click()
    time.sleep(2)
    assert page_tables.added_row.exist()
    page_tables.btn_delete_row.click()
    assert not page_tables.added_row.exist()

def test_table_pages(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.btn_rows_qty.click()
    page_tables.option_5_rows.click()
    page_tables.btn_next.get_dom_attribute('disabled')
    page_tables.btn_previous.get_dom_attribute('disabled')

    for i in range(3):
        page_tables.btn_add.click()
        time.sleep(2)
        assert page_tables.registration_form.exist()
        page_tables.registration_form_submit_btn.click()
        assert page_tables.registration_form.exist()
        page_tables.registration_form_first_name.send_keys('Aleksey')
        page_tables.registration_form_last_name.send_keys('Grebeshkov')
        page_tables.registration_form_email.send_keys('grebeshkov@gmail.com')
        page_tables.registration_form_age.send_keys('35')
        page_tables.registration_form_salary.send_keys('25000')
        page_tables.registration_form_department.send_keys('BUH')
        page_tables.registration_form_submit_btn.click()
        time.sleep(2)

    assert page_tables.total_pages_qty.get_text() == '2'
    page_tables.btn_next.click()
    assert page_tables.current_pages_qty.get_dom_attribute('value') == '2'
    page_tables.btn_previous.click()
    assert page_tables.current_pages_qty.get_dom_attribute('value') == '1'






