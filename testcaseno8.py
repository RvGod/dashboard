from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Setup Chrome
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:
    #Log in
    driver.get("http://localhost/dashboard/expense_tracker/login_page.php")
    time.sleep(2)

    driver.find_element(By.NAME, "email").send_keys("sample@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("pass1234")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    #Go to History page
    driver.find_element(By.XPATH, "//li[span[text()='History']]").click()
    time.sleep(2)

    #Store the first row text before deletion
    first_row = driver.find_element(By.CSS_SELECTOR, "#history-body tr:first-child")
    first_row_text = first_row.text

    #Delete the first transaction row
    first_row.find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    #Accept the confirmation alert
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)

    #Verify the first row is removed
    history_rows = driver.find_elements(By.CSS_SELECTOR, "#history-body tr")
    if history_rows and history_rows[0].text == first_row_text:
        print("TC008 FAIL: First transaction was not deleted.")
    else:
        print("TC008 PASS: First transaction deleted successfully.")

finally:
    time.sleep(2)
    driver.quit()
