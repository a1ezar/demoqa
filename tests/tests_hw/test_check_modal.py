from pages.modal_dialogs import ModalDialog
import time

def test_small_modal_dialog(browser):
    modal_page = ModalDialog(browser)
    modal_page.visit()

    assert modal_page.small_modal_button.exist()
    modal_page.small_modal_button.click()
    time.sleep(2)

    assert modal_page.small_modal.exist()
    assert modal_page.small_modal.visible()

    modal_page.small_modal_close_button.click()
    time.sleep(2)
    
    assert not modal_page.small_modal.exist()

def test_large_modal_dialog(browser):
    modal_page = ModalDialog(browser)
    modal_page.visit()

    assert modal_page.large_modal_button.exist()
    modal_page.large_modal_button.click()
    time.sleep(2)

    assert modal_page.large_modal.exist()
    assert modal_page.large_modal.visible()

    modal_page.large_modal_close_button.click()
    time.sleep(2)
    
    assert not modal_page.large_modal.exist()