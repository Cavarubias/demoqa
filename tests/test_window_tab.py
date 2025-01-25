from pages.links import Links
import time

def test_links(browser):
    links_page = Links(browser)
    links_page.visit()

    links_page.link_home.click()
    time.sleep(3)
    pages_qty = len(browser.window_handles)
    assert pages_qty == 2