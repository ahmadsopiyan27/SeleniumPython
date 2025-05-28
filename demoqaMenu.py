from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

driver.maximize_window()

driver.get('https://demoqa.com/menu')


sub_sublist = driver.find_element(By.XPATH,"//a[contains(text(),'Main Item 2')]")
sub_item2 = driver.find_element(By.XPATH,"//a[contains(text(),'SUB SUB LIST »')]")
menu_item2 = driver.find_element(By.XPATH,"//a[contains(text(),'Sub Sub Item 2')]")

action = ActionChains(driver)
action.move_to_element(sub_sublist)
action.move_to_element(sub_item2)
action.perform()


try:
    WebDriverWait(driver,3).until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(text(),'Sub Sub Item 2')]")))
    sub_item2.click

except TimeoutException:
    print('gk muncul bang')
    pass
