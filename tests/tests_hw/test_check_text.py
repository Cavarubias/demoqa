from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text.get_text()
    demo_qa_page.button_element.click()
    elements_page.visit()
    assert elements_page.equal_url()
    assert elements_page.text.get_text()