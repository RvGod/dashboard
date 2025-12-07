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
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("pass1234")
    time.sleep(2)
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    #Click Budget in sidebar
    driver.find_element(By.XPATH, "//li[span[text()='Budget']]").click()
    time.sleep(2)

    #Enter a valid budget
    budget_input = driver.find_element(By.ID, "budget-input")
    time.sleep(1)
    budget_input.clear()
    budget_input.send_keys("5000")
    time.sleep(1)

    #Click Save Budget
    driver.find_element(By.XPATH, "//button[text()='Save Budget']").click()
    time.sleep(2)
    
    #Verify the alert
    try:
        alert = Alert(driver)
        alert_text = alert.text
        if alert_text == "Budget Saved!":
            print("Alert appeared confirming budget saved")
        else:
            print(f"Unexpected alert text: {alert_text}")
        alert.accept()
    except:
        print("No alert appeared")
    time.sleep(2)  

    budget_input = driver.find_element(By.ID, "budget-input")
    if budget_input.get_attribute("value") == "":
        print("TC004 PASS: Budget input field is cleared after saving")
    else:
        print(f"TC004 FAIL: Budget input field is not cleared, value = {budget_input.get_attribute('value')}")

finally:
    time.sleep(2)
    driver.quit()
