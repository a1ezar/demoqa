from pages.base_page import BasePage
from components.components import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time



class Tables(BasePage):
    
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        
        self.no_data = WebElement(driver, '#div.rt-noData')
        self.button_delete_row = WebElement(driver, '#delete-record-')
        self.add_button = WebElement(driver, '#addNewRecordButton')
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.submit_button = WebElement(driver, '#submit')
        self.page_rows = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.five_rows =  WebElement(driver, "//*[contains(text(), '5 rows')]", 'xpath')
        self.next_button = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-next > button')
        self.previous_button = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-previous > button')
        self.total_pages = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > span')
        self.current_page = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.-pageInfo > div > input[type=number]')
        
    def record_exists(self, first_name: str, last_name: str) -> bool:
        try:
            first = self.driver.find_element(
                By.XPATH, f"//div[@class='rt-td' and text()='{first_name}']"
            )
            last = self.driver.find_element(
                By.XPATH, f"//div[@class='rt-td' and text()='{last_name}']"
            )
            return first.is_displayed() and last.is_displayed()
        except NoSuchElementException:
            return False
        
    def edit_button_for(self, first_name: str) -> WebElement:
        return WebElement(
            self.driver,
            f"//div[@class='rt-tr-group'][.//div[@class='rt-td' and text()='{first_name}']]//span[@title='Edit']",
            locator_type="xpath"
        )

    def delete_button_for(self, first_name: str) -> WebElement:
        return WebElement(
            self.driver,
            f"//div[@class='rt-tr-group'][.//div[@class='rt-td' and text()='{first_name}']]//span[@title='Delete']",
            locator_type="xpath"
        )
        
    def add_record(self):
        self.add_button.click_force()
        time.sleep(2)
        self.first_name.send_keys('tester')
        self.last_name.send_keys('testerov')
        self.email.send_keys('test@test.ru')
        self.age.send_keys('21')
        self.salary.send_keys('1111111111111111')
        self.department.send_keys('IT')
        self.submit_button.click_force()
        time.sleep(2)