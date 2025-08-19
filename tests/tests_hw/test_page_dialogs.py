from pages.modal_dialogs import ModalDialog

def test_modal_elements(browser):
    modal_dialog_page = ModalDialog(browser)
    modal_dialog_page.visit()
    
    assert modal_dialog_page.buttons_third_menu.check_count_elemets(count = 5)
    
def test_navigation_modal(browser):
    modal_dialog_page = ModalDialog(browser)
    modal_dialog_page.visit()
    
    modal_dialog_page.refresh()
    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert modal_dialog_page.get_url() == 'https://demoqa.com/'
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
