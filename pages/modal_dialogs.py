from pages.base_page import BasePage
from components.components import WebElement

class ModalDialog(BasePage):
    
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        
        self.buttons_third_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a')
        self.small_modal_button = WebElement(driver, '#showSmallModal')
        self.large_modal_button = WebElement(driver, '#showLargeModal')
        self.small_modal_close_button = WebElement(driver, '#closeSmallModal')
        self.large_modal_close_button = WebElement(driver, '#closeLargeModal')
        self.small_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.large_modal = WebElement(driver, '#example-modal-sizes-title-lg')