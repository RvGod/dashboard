from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:
    #Open index.php directly without login
    driver.get("http://localhost/dashboard/expense_tracker/index.php")
    time.sleep(2)

    #Check if redirected to login page
    current_url = driver.current_url
    if "login_page.php" in current_url:
        print("TC009 PASS: Unauthorized access redirected to login page.")
    else:
        print(f"TC009 FAIL: Current page is {current_url}")

finally:
    time.sleep(2)
    driver.quit()
