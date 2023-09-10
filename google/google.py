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
import autoit
from time import sleep

async def main(dname, demail, rfname, rlname, remail, addr, city, country, zip, date, payee, addtional):
  chrome_options = Options()
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  wait = WebDriverWait(driver, 20)
  driver.get('https://support.google.com/accounts/troubleshooter/6357590?hl=en')
  
  driver.find_element(By.CSS_SELECTOR,'span[aria-label="Submit a request for funds from a deceased user\'s account"]').click()

  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Full name of the deceased person"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Full name of the deceased person"]').send_keys(dname)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Email address of the deceased person"]').send_keys(demail)
  
  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="First name of relative/legal representative"]').send_keys(rfname)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Last name of relative/legal representative"]').send_keys(rlname)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Email address of relative/legal representative"]').send_keys(remail)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Address"]').send_keys(addr)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="City"]').send_keys(city)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Zip code"]').send_keys(zip)
  
  driver.find_elements(By.CSS_SELECTOR, 'input[aria-label="Date of death"]')[0].send_keys(date)
  driver.find_elements(By.CSS_SELECTOR, 'input[aria-label="Date of death"]')[1].send_keys(date)

  driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Desired payee name for the account"]').send_keys(payee)

  driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Choose files"]').click()

  
  autoit.win_wait_active("Open")
  file_route = os.path.join(os.getcwd(), 'doc.png')
  
  autoit.control_send("Open", "Edit1", 'C:\\dev\\trustle\\trustle-bot\\google\\doc.png')
  # autoit.control_send("Open", "Open", "{ENTER}")
  # driver.find_element(By.CSS_SELECTOR, 'input[id="documents"]').send_keys(os.path.join(os.getcwd(), 'doc.png'))
  # sleep(5)
  # driver.find_element(By.CSS_SELECTOR, 'input[id="documents"]').send_keys(os.path.join(os.getcwd(), 'deathcert.png'))
  # sleep(5)
  # driver.find_element(By.CSS_SELECTOR, 'input[id="documents"]').send_keys(os.path.join(os.getcwd(), 'id.png'))
  
  sleep(60)

asyncio.run(main('dname', 'demail', 'rfname', 'rlname', 'remail', 'addr', 'city', 'country', 'zip', '9/10/2023', 'payee', 'addtional'))