from pages.text_box import TextBox
import time

def test_text_box(browser):
    text_box = TextBox(browser)
    full_name = 'Aleksey'
    current_address = 'Saint-Petersburg, Nevsky pr., 1'

    text_box.visit()
    text_box.full_name.send_keys(full_name)
    text_box.current_address.send_keys(current_address)
    text_box.submit_btn.click()
    time.sleep(5)
    assert text_box.output_name.get_text() == 'Name:' + full_name
    assert text_box.output_address.get_text() == 'Current Address :' + current_address