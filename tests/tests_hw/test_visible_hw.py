from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    
    assert accordion_page.first_section.visible()
    
    accordion_page.heading.click()
    time.sleep(3)
    assert not accordion_page.first_section.visible()
    
def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)
    accordion_page.visit()
    
    assert not accordion_page.second_section_first.visible()
    assert not accordion_page.second_section_second.visible()
    assert not accordion_page.third_section.visible()