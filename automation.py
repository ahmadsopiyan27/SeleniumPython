from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.maximize_window()

driver.get('https://www.saucedemo.com/')


driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
# driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
sleep(3)
# title = driver.find_element(By.XPATH,"//div[@class='app_logo']").text
# print(title)
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
confirmation_text = driver.find_element(By.CLASS_NAME, "complete-header").text
print("Status Checkout:", confirmation_text)
