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

mneu_item2 = driver.find_element(By)

try:
    WebDriverWait(driver,5).until(EC.alert_is_present())
    print('alert muncul bang')

except TimeoutException:
    print('gk muncul bang')
    pass
