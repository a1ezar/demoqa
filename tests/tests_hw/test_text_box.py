from pages.text_box import TextBox
import time

def test_fill_form(browser):
    text_box = TextBox(browser)
    text_box.visit()
    
    name = 'test'
    address = 'testov'
    text_box.full_name.send_keys(name)
    text_box.current_address.send_keys(address)
    time.sleep(3)
    text_box.button_submit.click_force()
    time.sleep(3)
    assert text_box.name_output.get_text() == 'Name:' + name
    assert text_box.address_output.get_text() == 'Current Address :' + address
