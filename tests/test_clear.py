from pages.text_box import TextBox
import time

def test_form_page(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('Aleksey')
    time.sleep(2)
    text_box.full_name.clear()
    time.sleep(2)
    assert text_box.full_name.get_text() == ''