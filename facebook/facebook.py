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

async def main(email, represent, minor, legaldoc, fullname, mailing,URL):
  chrome_options = Options()
  driver = webdriver.Chrome(options=chrome_options)
  driver.maximize_window()
  driver.get('https://www.facebook.com/help/contact/398036060275245')

  # sleep(10)
  wait = WebDriverWait(driver, 10)
  # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.uiInputLabelInput.clearfix')))
  # print(len(driver.find_elements(By.CSS_SELECTOR, 'div.uiInputLabelInput.clearfix')))

  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="Field524156021329732"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[name="Field524156021329732"]').send_keys(email)
  
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="IDupload[]"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[name="IDupload[]"]').send_keys(os.path.join(os.getcwd(), 'id.png'))

  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="DocumentUpload[]"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[name="DocumentUpload[]"]').send_keys(os.path.join(os.getcwd(), 'doc.png'))

  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="DeathCertificateUpload[]"]')))
  driver.find_element(By.CSS_SELECTOR, 'input[name="DeathCertificateUpload[]"]').send_keys(os.path.join(os.getcwd(), 'deathcert.png'))

  sleep(4)
  
  if represent:
    driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[0].click()

    if minor:
      driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[2].click()
      driver.find_element(By.CSS_SELECTOR, 'label._kv1._55sg.uiInputLabelInput').click()
      
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field186073084863833"]').send_keys(fullname)
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field294236104030503"]').send_keys(mailing)
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field144852172330431"]').send_keys(URL)
      
    else:
      wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')))
      driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[3].click()
      
      if legaldoc:
        driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[4].click()
        
      else :
        driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[5].click()
      
      driver.find_element(By.CSS_SELECTOR, 'label._kv1._55sg.uiInputLabelInput').click()
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field186073084863833"]').send_keys(fullname)
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field294236104030503"]').send_keys(mailing)
      driver.find_element(By.CSS_SELECTOR, 'input[name="Field144852172330431"]').send_keys(URL)
      
  else:
    driver.find_elements(By.CSS_SELECTOR, 'label._55sh.uiInputLabelInput')[1].click()
  
  driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
  
asyncio.run(main('trustle@com', True, False, True , 'trustle', 'test', 'mainurl'))