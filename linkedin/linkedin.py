# Importing necessary libraries
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

# Defining the main function with parameters
async def main(fname, lname, email, dname, durl, relationship, demailaddr, date, article, info, signature):
  
  # Configure Chrome options
  chrome_options = Options()
  
  # Initialize the Chrome WebDriver
  driver = webdriver.Chrome(options=chrome_options)
  
  # Maximize the browser window
  driver.maximize_window()
  
  # Navigate to the LinkedIn help page
  driver.get('https://www.linkedin.com/help/linkedin/ask/TS-RDMLP')
  
  # Fill in the first name field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-firstname"]').send_keys(fname)

  # Fill in the last name field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-lastname"]').send_keys(lname)

  # Fill in the email field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-email"]').send_keys(email)

  # Fill in the deceased name field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-deceased_name"]').send_keys(dname)
  
  # Scroll down the page by 400 pixels
  driver.execute_script(f"window.scrollBy(0, 400);")
  
  # Fill in the deceased profile URL field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-deceased_profile_url"]').send_keys(durl)

  # Select the relationship option by clicking on it (assuming it's the third option)
  driver.find_element(By.CSS_SELECTOR, 'li[id="option-relationship_to_deceased-3"]').click()

  # Fill in the other relationship field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-other_relationship"]').send_keys(relationship)

  # Fill in the deceased email address field
  driver.find_element(By.CSS_SELECTOR, 'input(id="dyna-deceased_email_addr"]').send_keys(demailaddr)

  # Fill in the date of deceased field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-date_deceased"]').send_keys(date)

  # Fill in the obituary or article field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-obit_or_article"]').send_keys(article)

  # Fill in the additional information field (assuming it's a textarea)
  driver.find_element(By.CSS_SELECTOR, 'textarea[id="dyna-addl_info"]').send_keys(info)
  
  # Scroll down the page by another 400 pixels
  driver.execute_script(f"window.scrollBy(0, 400);")
  
  # Fill in the signature field
  driver.find_element(By.CSS_SELECTOR, 'input[id="dyna-signature"]').send_keys(signature)

  # Click on the reCAPTCHA checkbox
  driver.find_element(By.CSS_SELECTOR, 'div.recaptcha-checkbox-border').click()

  # Click on the form submit button
  driver.find_element(By.CSS_SELECTOR, 'button[id="dynaform-submit"]').click()

# Run the main function with sample data
asyncio.run(main('fname', 'lname', 'email', 'dname', 'durl', 'relationship', 'demailaddr', 'date', 'article', 'info', 'signature'))
