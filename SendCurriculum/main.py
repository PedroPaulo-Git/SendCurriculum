import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
# click to enter account
wait = WebDriverWait(driver, 20)
login_click = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn__primary--large.from__button--floating")))
login_click.click()
#nav until jobs
# nav_jobs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]')))
# nav_jobs.click()



def applying_job():
    job_list = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"ul.scaffold-layout__list-container > li")))

    print(f"Number of jobs found: {len(job_list)}")

    for index, job in enumerate(job_list):
        try:
            choose = job.find_element(By.TAG_NAME,"a")
            print(f"Job {index + 1}: {choose.text}")
            choose.click()
            #trying apply candidature >
            print("Applying on this job")
            click_button_candidature = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.jobs-apply-button")))
                    #driver.find_element((By.CSS_SELECTOR, "button.jobs-apply-button"))
                    #click to apply
            click_button_candidature.click()

                    #############Fisrt Next button
            print("Fisrt Next button")
            while True:
                try:
                    
                    click_button_candidature_next = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-easy-apply-next-button]"))
                    )


                    ############# second Next button
                    print("second Next button")
                    click_button_candidature_next.click()
                    click_button_candidature_next = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-easy-apply-next-button]"))
                    )


                    ########### third Next button
                    print("third Next button")
                    click_button_candidature_next.click()

                    ########### options
                    select_option =  WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-test-text-selectable-option='0'] input"))
                    )
                    select_option.click()
                    print("select_option button AFTER")

                except:
                    print("CHOOSE DONT APPLYING")
                    #driver.quit()
                           
        except Exception as e:
            print(f"error with job {index+1}:{e}")
            
        time.sleep(3)





Change_candidature = False
def change_candidature():
    global Change_candidature
    #nav until jobs
    nav_jobs = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]')))
    nav_jobs.click()
    locate = input("Which state or country ? ").strip()
    locate_default = "Brazil"

    stack = input("Which stack or job do you want ? ").strip()
    stack_default = "Full-stack"
    put_locate = driver.find_element(By.XPATH,"//input[contains(@id, 'jobs-search-box-location-id')]")
    #search input stack
    put_stack = driver.find_element(By.XPATH,"//input[contains(@id,'jobs-search-box-keyword-id')]")


    if locate == "" and stack == "":
        put_locate.clear()
        put_stack.send_keys(stack_default)
        put_locate.send_keys(locate_default + Keys.ENTER)
    else :
        put_locate.clear()
        put_stack.send_keys(stack)
        put_locate.send_keys(locate + Keys.ENTER)
        time.sleep(2)

    print(locate)
    print(stack)
    #in jobs
    #now the ask or not
    candidature = input("Your current candidature is Incorrect ? Y or N ")
    if candidature.lower() == "y":
        Change_candidature = True
        print("change candidature? ",Change_candidature)
        driver.get("https://linkedin.com")     
    elif candidature.lower() == "n":
        Change_candidature = False
        print("change candidature? ",Change_candidature)
        print("starting applying job..")
        applying_job()
    else:
        candidature = input("INVALID INPUT | Your current candidature is correctly ? Y or N ")
        driver.get("https://linkedin.com")
        change_candidature()




if not Change_candidature: 
   
  change_candidature()


    #search input locate
   
else:
    print('trying...')









    
time.sleep(222)

driver.quit()