from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import time

#Setup Chrome
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:
    #Open login page and log in
    driver.get("http://localhost/dashboard/expense_tracker/login_page.php")
    time.sleep(2)

    driver.find_element(By.NAME, "email").send_keys("sample@gmail.com")
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys("pass1234")
    time.sleep(1)
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    #Click Transaction in sidebar
    driver.find_element(By.XPATH, "//li[span[text()='Add Transaction']]").click()
    time.sleep(2)

    #Leave all required fields blank and click Add
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(1)

    #Check for alert
    try:
        alert = Alert(driver)
        alert_text = alert.text
        if "Please fill in all required fields" in alert_text:
            print(f"TC006 PASS: Alert triggered correctly: '{alert_text}'")
        else:
            print(f"TC006 FAIL: Unexpected alert text: '{alert_text}'")
        alert.accept()
    except:
        print("TC006 FAIL: No alert displayed for empty required fields.")

finally:
    time.sleep(2)
    driver.quit()
