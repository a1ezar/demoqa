from pages.alerts import Alert
import time

def test_timer_alert(browser):
    alert_page = Alert(browser)
    alert_page.visit()
    
    assert alert_page.timer_alert_button.exist()
    assert not alert_page.alert()

    alert_page.timer_alert_button.click()
    time.sleep(2)
    assert not alert_page.alert()
    
    time.sleep(2)
    assert not alert_page.alert()
    
    time.sleep(1)
    assert alert_page.alert()
    
    alert_page.alert().accept()
    assert not alert_page.alert() 