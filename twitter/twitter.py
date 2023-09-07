from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
import asyncio
import json
import os
from time import sleep

# Define the main function that will be executed asynchronously
async def main(fullname, email, tname, owener, info):
  # Configure Chrome options
  chrome_options = Options()
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.get('https://help.twitter.com/en/forms/account-access/deactivate-or-close-account/deactivate-account-for-deceased')

  options = driver.find_elements(By.CSS_SELECTOR, 'input[name="Category__c"]')
  options[0].click()
  
  driver.execute_script(f"window.scrollBy(0, 400);")
  
  driver.find_element(By.CSS_SELECTOR, 'input[name="Form_Name__c"]').send_keys(fullname)
  driver.find_element(By.CSS_SELECTOR, 'input[name="Form_Email__c"]').send_keys(email)

  driver.execute_script(f"window.scrollBy(0, 400);")

  options = driver.find_elements(By.CSS_SELECTOR, 'input[name="Relationship_to_User__c"]')
  options[1].click()

  driver.find_element(By.CSS_SELECTOR, 'input[name="Reported_Screen_Name__c"]').send_keys(tname)
  driver.find_element(By.CSS_SELECTOR, 'input[name="owner-full-name"]').send_keys(owener)

  if len(info) > 0:
    driver.find_element(By.CSS_SELECTOR, 'textarea[name="DescriptionText"]').send_keys(info)
  
  driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
  

  sleep(60)

asyncio.run(main('fullname', 'email', 'tname', 'taccount', 'optional'))