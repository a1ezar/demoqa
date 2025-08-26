from pages.links import Links
import time

def test_home_link(browser):
    links_page = Links(browser)
    links_page.visit()
  
    assert links_page.home_link.exist()
    assert links_page.home_link.get_text() == "Home"
    assert links_page.home_link.get_dom_attribute('href') == "https://demoqa.com"
    
    initial_tabs = len(browser.window_handles)
    links_page.home_link.click()
    time.sleep(2)
    new_tabs = len(browser.window_handles)
    assert new_tabs == initial_tabs + 1