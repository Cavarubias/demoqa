from pages.accordion import AccordionPage
import time

def test_visible_accordion(browser):
    accordion_page = AccordionPage(browser)

    accordion_page.visit()
    assert accordion_page.lorem_ipsum_text.visible()
    accordion_page.lorem_ipsum_title.click()
    time.sleep(2)
    assert not accordion_page.lorem_ipsum_text.visible()

def test_visible_accordion_default(browser):
    accordion_page = AccordionPage(browser)

    accordion_page.visit()
    assert not accordion_page.where_does_it_come_from_text_first_paragraph.visible()
    assert not accordion_page.where_does_it_come_from_text_second_paragraph.visible()
    assert not accordion_page.why_do_we_use_it_text.visible()