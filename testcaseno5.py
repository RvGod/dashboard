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

    #Click Categories in sidebar
    driver.find_element(By.XPATH, "//li[span[text()='Categories']]").click()
    time.sleep(2)

    #Enter a new category
    new_category_input = driver.find_element(By.ID, "new-category")
    new_category_input.clear()
    new_category_input.send_keys("Food")#First attempt
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Add Category']").click()
    time.sleep(2)

    #Attempt to add duplicate category
    new_category_input = driver.find_element(By.ID, "new-category")
    new_category_input.clear()
    new_category_input.send_keys("Food") #Duplicate attempt
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Add Category']").click()
    time.sleep(2)

    #Check for alert(duplicate should trigger alert)
    try:
        alert = Alert(driver)
        alert_text = alert.text
        if "already exists" in alert_text or "cannot be empty" in alert_text:
            print(f"TC005 PASS: Duplicate category prevented. Alert: '{alert_text}'")
        else:
            print(f"TC005 FAIL: Unexpected alert: '{alert_text}'")
        alert.accept()
    except:
        # No alert, check if duplicate appeared in category list
        category_list_items = driver.find_elements(By.CSS_SELECTOR, "#category-list li")
        count = sum("Food" in li.text for li in category_list_items)
        if count > 1:
            print("TC005 FAIL: Duplicate category was added!")
        else:
            print("TC005 PASS: Duplicate category prevented in list")

finally:
    time.sleep(2)
    driver.quit()
