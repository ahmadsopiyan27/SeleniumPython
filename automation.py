from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.maximize_window()

driver.get('https://www.saucedemo.com/')


driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click
title = driver.find_element(By.XPATH,'//*[@id="header_container"]/div[1]/div[2]/div').text
print(title)

print()