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

driver.get('https://www.ozon.ru/ozonid')
WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, AUTH_FORM)))
driver.find_element(By.XPATH, INPUT_FORM).send_keys("9009295422")
auth = driver.find_element(By.XPATH, AUTH_FORM)
auth.find_element(By.XPATH, SIGN_IN_BUTTON).click()


if input():
    driver.quit()
