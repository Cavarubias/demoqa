from pages.demoqa import DemoQa
from pages.accordion import AccordionPage
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time

@pytest.mark.parametrize("pages", [AccordionPage, Alerts, BrowserTab, DemoQa])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.viewport.exist()
    assert page.viewport.get_dom_attribute('name') == 'viewport'
    assert page.viewport.get_dom_attribute('content') == 'width=device-width,initial-scale=1'