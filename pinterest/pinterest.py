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

async def main(fname, sname, username, email, option, altemail):
  chrome_options = Options()
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.get('https://help.pinterest.com/en-gb/contact?current_page=about_you_page&account_access=close_account&page=overview_page_1')
  
  driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-user-first-name"]').send_keys(fname)

  driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-user-last-name"]').send_keys(sname)

  driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-user-username"]').send_keys(username)

  driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-user-email"]').send_keys(email)

  driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-actions-about-you-1-wizard-next"]').click()

  if option:
    driver.find_element(By.CSS_SELECTOR,'label[for="edit-user-email-access-yes"]').click()
    
  else:
    driver.find_element(By.CSS_SELECTOR,'label[for="edit-user-email-access-no"]').click()
    
    driver.find_element(By.CSS_SELECTOR,'input[data-drupal-selector="edit-user-other-emails-items-0-item-"]').send_keys(altemail)
    

  sleep(60)

asyncio.run(main('fname', 'sname', 'username', 'alexgector@gmail.com',False, 'alter@gmail.com'))