from pages.text_box import TextBox
import time

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'