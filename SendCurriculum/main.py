import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://linkedin.com")

time.sleep(101)

driver.quit()