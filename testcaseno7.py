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
    driver.find_element(By.NAME, "password").send_keys("pass1234")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    #Click Transaction in sidebar
    driver.find_element(By.XPATH, "//li[span[text()='Add Transaction']]").click()
    time.sleep(2)

    #Fill transaction form
    driver.find_element(By.ID, "amount").send_keys("100")
    driver.find_element(By.ID, "type").send_keys("expense")
    driver.find_element(By.ID, "category").send_keys("Food")
    driver.find_element(By.ID, "date").send_keys("01-01-2025")
    driver.find_element(By.ID, "description").send_keys("Lunch")
    time.sleep(1)

    #Click Add button
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)

    #Handle alert
    try:
        alert = Alert(driver)
        alert_text = alert.text
        if "Transaction Added" in alert_text:
            print(f"Alert displayed correctly: '{alert_text}'")
        else:
            print(f"Unexpected alert text: '{alert_text}'")
        alert.accept()
    except:
        print("No alert displayed after adding transaction")

    #Verify transaction in history
    driver.find_element(By.XPATH, "//li[span[text()='History']]").click()
    time.sleep(2)

    history_rows = driver.find_elements(By.CSS_SELECTOR, "#history-body tr")
    transaction_found = False
    for row in history_rows:
        if "100" in row.text and "expense" in row.text and "Food" in row.text:
            transaction_found = True
            break

    if transaction_found:
        print("TC007 PASS: Transaction appears correctly in history")
    else:
        print("TC007 FAIL: Transaction not found in history")

finally:
    time.sleep(2)
    driver.quit()
