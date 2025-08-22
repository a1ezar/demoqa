from pages.text_box import TextBox
import time

def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()
    
    text_box.full_name.send_keys('test')
    time.sleep(3)
    text_box.full_name.clear()
    time.sleep(3)
    assert text_box.full_name.get_text() == ''
    
    