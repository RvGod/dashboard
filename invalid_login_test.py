from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Setup browser
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

#Open login page 
driver.get("http://localhost/dashboard/expense_tracker/login_page.php")
time.sleep(3)

#Enter invalid credentials
driver.find_element(By.NAME, "email").send_keys("wrong@gmail.com")  # Invalid email
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("wrongpass")     # Invalid password
time.sleep(2)

#3. Click login button
driver.find_element(By.NAME, "login").click()
time.sleep(3)

#Verify error message
error_element = driver.find_elements(By.CLASS_NAME, "error")

if error_element and "Invalid" in error_element[0].text:
    print("Test passed: Error message displayed")
else:
    print("Test failed: No error message displayed")

time.sleep(2)
driver.quit()
