from selenium.webdriver.support.wait import WebDriverWait

from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains



import time

driver = Driver()

LOGIN_LOGO = "//div[@class='fac7']"
NUMBER_INPUT = "//input[@class='d00-a d00-a3 az9b d00-a4']"
NUMBER_DIV_CLICKED = "//div[@class='f00-a f00-a7 f00-b6 f00-b4 azb9']"
NUMBER_DIV_UNCLICKED="//div[@class='f00-a f00-a7 f00-b6 azb9']"
LOGIN_BUTTON = "//button[@class='b200-a0 b200-b5 b200-b2 b200-a4']"
NINES = "/html/body/div[1]/div/div[1]/div/div/div[4]/div/div/div[1]/label/div/div/p"
LOGIN_BUTTON_X = "/html/body/div[1]/div/div[1]/div/div/div[5]/button"
AUTH_FRAME = "//iframe[@id='authFrame']"

driver.get('https://www.ozon.ru/')
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, LOGIN_LOGO)))
driver.find_element(By.XPATH, LOGIN_LOGO).click()
print(driver.page_source)
# form = driver.find_element(By.XPATH, AUTH_FRAME)
# tel = form.find_element(By.TAG_NAME, "input")
# tel.send_keys('9204669750')
# actions = ActionChains(driver)
# actions.send_keys('9204669750')
# actions.perform()


if input():
    driver.quit()
