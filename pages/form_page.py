from pages.base_page import BasePage
from components.components import WebElement

class FormPage(BasePage):
    
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form' 
        super().__init__(driver, self.base_url)
        
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.button_submit = WebElement(driver, '#submit')
        self.modal_dialog = WebElement(driver, '#body > div.fade.modal.show > div')
        self.button_close_modal = WebElement(driver, '#closeLargeModal')
        self.user_form = WebElement(driver, '#userForm')
        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')
        self.state = WebElement(driver, '#state')
        self.city = WebElement(driver, '#city')
        self.NCR =  WebElement(driver, "//*[contains(text(), 'NCR')]", 'xpath')
        self.delhi = WebElement(driver, "//*[contains(text(), 'Delhi')]", 'xpath')
        
