from selenium.webdriver import Keys
from pages.slider import Slider
import time

def test_slider(browser):
    slider_page = Slider(browser)
    slider_page.visit()

    assert slider_page.slider.exist()
    assert slider_page.slider_value.exist()
    assert slider_page.slider_value.get_dom_attribute('value') == '25'

    while not slider_page.slider_value.get_dom_attribute('value') == '50':
        slider_page.slider.send_keys(Keys.ARROW_RIGHT)

    assert slider_page.slider_value.get_dom_attribute('value') == '50'