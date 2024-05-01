from auto_chromedriver.driver import Driver
from selenium.webdriver import ChromeOptions
from email_tools.generator.Generators import generate_login, generate_password
from email_tools.data.tuta_xpath_config import XPATH_SignUp, Email_State
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


class Tuta:
    def __init__(self, time_delay: int = 5):
        self.time_delay = time_delay

    def generate_account(self):
        options = ChromeOptions()
        options.add_argument("--lang=en")

        driver = Driver(options=options)

        driver.get(XPATH_SignUp.StartPage)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_SignUp.LOGIN_FORM)))
        driver.find_element(By.XPATH, XPATH_SignUp.SIGN_UP_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_SignUp.ACCOUNT_PLAN_FORM)))
        time.sleep(self.time_delay)

        driver.find_element(By.XPATH, XPATH_SignUp.FREE_PLAN_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_SignUp.APPLY_RULES_DIALOG)))
        time.sleep(self.time_delay)

        driver.find_element(By.XPATH, XPATH_SignUp.CHECKBOX_1).click()
        driver.find_element(By.XPATH, XPATH_SignUp.CHECKBOX_2).click()
        driver.find_element(By.XPATH, XPATH_SignUp.RULES_OK_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_SignUp.EMAIL_LABEL)))
        time.sleep(self.time_delay)

        while True:
            login = generate_login()
            driver.find_element(By.XPATH, XPATH_SignUp.INPUT_EMAIL).send_keys(login)
            time.sleep(self.time_delay)

            login_state = self.get_email_state(driver)
            if login_state == Email_State.EMAIL_AVAILABLE:
                break
            driver.find_element(By.XPATH, XPATH_SignUp.INPUT_EMAIL).clear()
            time.sleep(self.time_delay)

        password = generate_password()
        driver.find_element(By.XPATH, XPATH_SignUp.INPUT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, XPATH_SignUp.REPEAT_PASSWORD).send_keys(password)
        driver.find_element(By.XPATH, XPATH_SignUp.SIGN_UP_CHECKBOX_1).click()
        driver.find_element(By.XPATH, XPATH_SignUp.SIGN_UP_CHECKBOX_2).click()
        driver.find_element(By.XPATH, XPATH_SignUp.NEXT_BUTTON).click()

        time.sleep(30)  # currently for capcha

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_SignUp.RECOVERY_WIZARD)))
        time.sleep(self.time_delay)

        recovery_code = ""
        recovery_element = driver.find_element(By.XPATH, XPATH_SignUp.RECOVERY_DIV)
        for i in range(1, 17):
            recovery_code += recovery_element.find_element(By.XPATH, f"span[{i}]").text

        print(f"Login: {login}")
        print(f"Password: {password}")
        print(f"Recovery code: {recovery_code}")

        time.sleep(self.time_delay)

        return login, password, recovery_code

    def get_email_state(self, driver: Driver):
        while True:
            login_state = driver.find_element(By.XPATH, XPATH_SignUp.EMAIL_TEXT).text
            if login_state == Email_State.EMAIL_AVAILABLE:
                return Email_State.EMAIL_AVAILABLE
            elif login_state == Email_State.EMAIL_TAKEN:
                return Email_State.EMAIL_TAKEN
            else:
                time.sleep(self.time_delay)
                continue


if __name__ == '__main__':
    Tuta().generate_account()
