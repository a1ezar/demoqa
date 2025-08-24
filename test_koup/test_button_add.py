from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    
    koup_page.visit()
    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    
    koup_page.link_add.click()
    assert koup_add.equal_url()
    
    assert koup_add.button_add.get_text() == 'Add Element'
    
    assert koup_add.button_add.get_dom_attribute('onclick') == 'addElement()'
    
    for i in range(4):
        koup_add.button_add.click()
        
    assert koup_add.buttons_delete.check_count_elemets(4)
    
    for element in koup_add.buttons_delete.find_elements():
        assert element.text == 'Delete'
    
    assert koup_add.buttons_delete.get_text() == 'Delete'
    
    while koup_add.buttons_delete.exist():
        koup_add.buttons_delete.click()
    
    assert not koup_add.buttons_delete.exist()