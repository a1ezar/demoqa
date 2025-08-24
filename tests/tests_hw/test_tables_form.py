from pages.tables import Tables
import time

def test_form(browser):
    tables_page = Tables(browser)
    tables_page.visit()
    
    assert not tables_page.modal_dialog.exist()
    tables_page.add_button.click_force()
    time.sleep(2)
    assert tables_page.modal_dialog.exist()
    
    tables_page.submit_button.click_force()
    time.sleep(2)
    assert tables_page.modal_dialog.exist() 
    
    tables_page.first_name.send_keys('tester')
    tables_page.last_name.send_keys('testerov')
    tables_page.email.send_keys('test@test.ru')
    tables_page.age.send_keys('21')
    tables_page.salary.send_keys('1111111111111111')
    tables_page.department.send_keys('IT')
    tables_page.submit_button.click_force()
    time.sleep(2)
    assert not tables_page.modal_dialog.exist()
    
    assert tables_page.record_exists("tester", "testerov")

    tables_page.edit_button_for("tester").click_force()
    tables_page.first_name.clear()
    tables_page.first_name.send_keys("updated")
    tables_page.submit_button.click_force()
    time.sleep(2)
    assert tables_page.record_exists("updated", "testerov")


    tables_page.delete_button_for("updated").click_force()
    assert not tables_page.record_exists("updated", "testerov")
    
def test_next_previous(browser):
    tables_page = Tables(browser)
    tables_page.visit()
    
    tables_page.page_rows.scroll_to_element()
    tables_page.page_rows.click()
    tables_page.five_rows.click()
    time.sleep(2)
    
    assert tables_page.next_button.get_dom_attribute('disabled')
    assert tables_page.previous_button.get_dom_attribute('disabled')
    
    for i in range(3):
        tables_page.add_record()
    time.sleep(2)
    
    assert tables_page.current_page.get_dom_attribute('value') == '1'
    assert tables_page.total_pages.get_text() == '2'
    
    tables_page.next_button.click()
    time.sleep(2)
    assert tables_page.current_page.get_dom_attribute('value') == '2'
    
    tables_page.previous_button.click()
    time.sleep(2)
    assert tables_page.current_page.get_dom_attribute('value') == '1'
