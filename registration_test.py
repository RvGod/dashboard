from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Setup browser
options = Options()

#ChromeDriver sometimes blocks requests or connections from local files or other origins due to Chrome’s security policies.
options.add_argument("--remote-allow-origins=*") 
driver = webdriver.Chrome(options=options)

#Open login page
driver.get("http://localhost/dashboard/expense_tracker/login_page.php")
time.sleep(3)

# Navigate to registration page
driver.find_element(By.LINK_TEXT, "Create an account").click()
time.sleep(3)

#Enter registration details
driver.find_element(By.NAME, "fullname").send_keys("Test User")        
time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("sample@gmail.com") 
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("pass1234")     
time.sleep(2)

#Click "Register" butto
driver.find_element(By.NAME, "register").click()  
time.sleep(5)

driver.quit()
