from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_footer_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.footer.equal_text('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.')
    
def test_centre_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    
    demo_qa_page.button_elements.click()
    assert elements_page.equal_url()
    
    assert elements_page.centre.equal_text('Please select an item from left to start practice.')