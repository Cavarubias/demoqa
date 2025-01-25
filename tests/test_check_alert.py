from pages.alerts import Alerts
import time

def test_timer_alert_button(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.time_alert_button.click()
    time.sleep(6)
    alert_page.alert().accept()
