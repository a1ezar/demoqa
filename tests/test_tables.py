from pages.tables import Tables
import time

def test_tables(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    assert not page_tables.no_data.exist()
    assert page_tables.button_delete_row.exist()
    
    while page_tables.button_delete_row.exist():
        page_tables.button_delete_row.click()
        
    assert page_tables.no_data.exist()