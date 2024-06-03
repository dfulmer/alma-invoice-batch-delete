from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Set up logging
from datetime import datetime
import logging

present = datetime.now()
now = present.strftime("%Y%m%d%H%M%S")
level    = logging.INFO
format   = '%(message)s'
handlers = [logging.FileHandler(f'{now}.log'), logging.StreamHandler()]
logging.basicConfig(level = level, format = format, handlers = handlers)

logging.info(f"Running {__file__} at: {present}")

driver = webdriver.Chrome()

# Go to Alma
# Sandbox
driver.get("https://umich-psb.alma.exlibrisgroup.com")

# Production
# driver.get("https://umich.alma.exlibrisgroup.com")

time.sleep(5)

#Log in
element = driver.find_element(By.ID,"username")
element.send_keys("almabot")
element = driver.find_element(By.ID,"password")
element.send_keys('')
element.submit()

time.sleep(15)

# Close the manage cookie preferences pop up
driver.find_element(By.ID,"onetrust-close-btn-container").click()

time.sleep(3)

# Set a counter, i, equal to 1. It will increase by one each time there is a problem or when there are no more invoices to delete, allowing for the program to end.
i = 1

while i < 75:
  try:
    # Go to Review(Invoice)
    ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys('1').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
    time.sleep(3)
    # Go to Unassigned (comment out the line below to stay at Assigned to Me)
    ActionChains(driver).key_down(Keys.ALT).send_keys('2').key_up(Keys.ALT).perform()
    time.sleep(3)
    # Get the invoice number and vendor and put them into variables
    invoicenumber = driver.find_element(By.ID,"SELENIUM_ID_invoiceList_ROW_0_COL_invoiceNumber")
    invoicevendor = driver.find_element(By.ID,"SELENIUM_ID_invoiceList_ROW_0_COL_vendorname")
    # Log what is being deleted
    logging.info(f'{invoicenumber.text}\t{invoicevendor.text}\t deleting at: {datetime.now()}')
    # Do the actual deletion. Click on the row actions list.
    driver.find_element(By.ID,"input_invoiceList_0").click()
    time.sleep(2)
    # Click Delete
    driver.find_element(By.XPATH,"//a[@title='Delete']").click()
    time.sleep(4)
    # Click Confirm
    driver.find_element(By.ID,"PAGE_BUTTONS_cbuttonconfirmationconfirm").click()
    time.sleep(18)
    # Comment in the following line to have the script stop after deleting the number of invoices n in the while i < n: line above.
    # i += 1
  except:
    # This means there was a problem or there are no more invoices to delete. Pause and increment the counter.
    logging.info(f"An issue arose... i = {i} {datetime.now()}")
    i += 1
    time.sleep(15)

time.sleep(2)
driver.quit()
logging.info(f'Ending...{datetime.now()}')
