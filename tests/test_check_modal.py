from conftest import browser
from pages.modal_dialogs import ModalDialogsPage
import time
import pytest

PAGE_CODE = ModalDialogsPage(browser).get_page_status()

@pytest.mark.skipif(PAGE_CODE != 200, reason='The page is unavailable')
def test_check_modal(browser):
    modal_dialogs_page = ModalDialogsPage(browser)
    modal_dialogs_page.visit()

    modal_dialogs_page.btn_small_modal.click()
    time.sleep(2)
    modal_dialogs_page.btn_close_small_modal.click()
    time.sleep(2)
    modal_dialogs_page.btn_large_modal.click()
    time.sleep(2)
    modal_dialogs_page.btn_close_Large_modal.click()
    time.sleep(2)
