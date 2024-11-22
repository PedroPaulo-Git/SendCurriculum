import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://linkedin.com")

input_element = driver.find_element(By.CLASS_NAME,"sign-in-form__sign-in-cta")
input_element.click()
#field email
username = os.getenv("LINKEDIN_EMAIL")
login_field_username = driver.find_element(By.ID,"username")
login_field_username.send_keys(username)
print(username)
# field password
password = os.getenv("LINKEDIN_PASSWORD")
login_field_password = driver.find_element(By.ID,"password")
login_field_password.send_keys(password)
#click to enter account

time.sleep(22)

driver.quit()