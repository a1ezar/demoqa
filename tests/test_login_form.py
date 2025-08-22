from pages.form_page import FormPage
from components.components import WebElement
import time

def  test_login_form(browser):
    form_page = FormPage(browser)
    form_page.visit()
    
    assert not form_page.modal_dialog.exist()
    time.sleep(3)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerov')
    form_page.user_email.send_keys('test@test.ru')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('1111111111111111')
    form_page.hobbies.click_force()
    form_page.current_address.send_keys('testing')
    time.sleep(3)
    form_page.button_submit.click_force()
    time.sleep(3)
    
    assert form_page.modal_dialog.exist()
    form_page.button_close_modal.click_force()
    
def test_fill_state_and_city(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    
    form_page.state.scroll_to_element()
    form_page.state.click()
    form_page.NCR.click()
    time.sleep(2)
    
    form_page.city.click()
    form_page.delhi.click()
    time.sleep(2)