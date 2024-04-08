from selenium.webdriver.support.wait import WebDriverWait

from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = Driver()

AUTH_FORM = "//section[@class='csma-ozon-id-page-anonymous']"
INPUT_FORM = "//input[@name='autocomplete']"
SIGN_IN_BUTTON_EN = "//button[@type='submit']/descendant::div[contains(text(), 'Sign in')]"
SIGN_IN_BUTTON_RU = "//button[@type='submit']/descendant::div[contains(text(), 'Войти')]"
SIGN_IN_BUTTON = "//button[@type='submit']"
CODE_INPUT = "//input[@name='otp']"

driver.get('https://www.ozon.ru/ozonid')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, AUTH_FORM)))
driver.find_element(By.XPATH, INPUT_FORM).send_keys("9204669750")
auth = driver.find_element(By.XPATH, AUTH_FORM)
auth.find_element(By.XPATH, SIGN_IN_BUTTON).click()
code = str(input())
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, CODE_INPUT)))
driver.find_element(By.XPATH, CODE_INPUT).send_keys(code)




if input():
    driver.quit()
