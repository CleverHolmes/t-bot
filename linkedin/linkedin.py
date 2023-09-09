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

async def main(fname, lname, email, dname, durl, relationship, demailaddr, date, article, info, signature):
  chrome_options = Options()
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.get('https://www.linkedin.com/help/linkedin/ask/TS-RDMLP')
  
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-firstname"]').send_keys(fname)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-lastname"]').send_keys(lname)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-email"]').send_keys(email)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-deceased_name"]').send_keys(dname)
  
  driver.execute_script(f"window.scrollBy(0, 400);")
  
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-deceased_profile_url"]').send_keys(durl)

  driver.find_element(By.CSS_SELECTOR, 'li[id="option-relationship_to_deceased-3"]').click()

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-other_relationship"]').send_keys(relationship)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-deceased_email_addr"]').send_keys(demailaddr)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-date_deceased"]').send_keys(date)

  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-obit_or_article"]').send_keys(article)

  driver.find_element(By.CSS_SELECTOR, 'textarea[id="dyna-addl_info"]').send_keys(info)
  
  driver.execute_script(f"window.scrollBy(0, 400);")
  
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-signature"]').send_keys(signature)

  driver.find_element(By.CSS_SELECTOR, 'div.recaptcha-checkbox-border').click()

  driver.find_element(By.CSS_SELECTOR, 'button[id="dynaform-submit"]').click()

asyncio.run(main('fname', 'lname', 'email', 'dname', 'durl', 'relationship', 'demailaddr', 'date', 'article', 'info', 'signature'))