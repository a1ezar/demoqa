from pages.tables import Tables
import time

def test_table_sorting(browser):
    tables_page = Tables(browser)
    tables_page.visit()
    
    assert not tables_page.no_data.exist()
    
    headers = [
        tables_page.first_name_header,
        tables_page.last_name_header,
        tables_page.age_header,
        tables_page.email_header,
        tables_page.salary_header,
        tables_page.department_header
    ]
    
    for header in headers:
        initial_class = tables_page.get_header_sort_class(header)
        header.click()
        time.sleep(2)
        
        after_click_class = tables_page.get_header_sort_class(header)
        assert after_click_class != initial_class
        
        header.click()
        time.sleep(2)
        after_second_click_class = tables_page.get_header_sort_class(header)
        assert after_second_click_class != after_click_class
