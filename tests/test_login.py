import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

html_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "login.html"))
driver.get("file://" + html_file)

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("secret")
driver.find_element(By.ID, "login-button").click()

message = driver.find_element(By.ID, "message").text

assert message == "Login successful", "Expected login to succeed"

driver.quit()
