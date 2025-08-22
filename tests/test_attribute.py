from pages.text_box import TextBox
import time

def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()
    
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'