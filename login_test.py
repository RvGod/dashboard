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

#Enter login credentials
driver.find_element(By.NAME, "email").send_keys("sample@gmail.com")  
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("pass1234")       
time.sleep(2)

#Click login button
driver.find_element(By.NAME, "login").click()
time.sleep(5) 

#Verify login
dashboard = driver.find_elements(By.ID, "dashboard")
if dashboard:
    print("Login successful")
else:
    print("Login failed")
    
time.sleep(2)
driver.quit()
