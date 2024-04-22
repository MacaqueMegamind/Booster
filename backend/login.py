from selenium.webdriver.support.wait import WebDriverWait
from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

from data.xpath_config import XPATHLoginEmail, XPATHLogin


class Login:
    def __init__(self, time_delay: int):
        self.driver = Driver()
        self.time_delay = time_delay

    def login_by_email(self, email: str):
        """
        Login by email and input email code if there is no ozone card
        :param email: Email
        """
        self.driver.get(XPATHLoginEmail.StartPage)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, XPATHLoginEmail.AUTH_FORM)))
        auth = self.driver.find_element(By.XPATH, XPATHLoginEmail.AUTH_FORM)
        auth.find_element(By.XPATH, XPATHLoginEmail.SIGN_IN_EMAIL_BUTTON).click()
        time.sleep(self.time_delay)
        self.driver.find_element(By.XPATH, XPATHLoginEmail.INPUT_FORM).send_keys(email)
        auth.find_element(By.XPATH, XPATHLoginEmail.SIGN_IN_BUTTON).click()
        time.sleep(self.time_delay)
        # здесь заменим потом int(input()) на получение кода из почты
        self.driver.find_element(By.XPATH, XPATHLoginEmail.INPUT_CODE_FORM).send_keys(int(input()))

        if input():
            self.driver.quit()

    def login_by_phone(self, number_phone: str):
        """
        Login by number phone and input code
        :param number_phone: number phone
        :return:
        """
        self.driver.get(XPATHLogin.StartPage)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, XPATHLogin.AUTH_FORM)))
        self.driver.find_element(By.XPATH, XPATHLogin.INPUT_FORM).send_keys(number_phone)
        auth = self.driver.find_element(By.XPATH, XPATHLogin.AUTH_FORM)
        auth.find_element(By.XPATH, XPATHLogin.SIGN_IN_BUTTON).click()
        time.sleep(self.time_delay)
        # здесь заменим потом int(input()) на получение кода с телефона
        self.driver.find_element(By.XPATH, XPATHLogin.INPUT_CODE_FORM).send_keys(int(input()))

        if input():
            self.driver.quit()


test = Login(time_delay=3)
# test.login_by_phone(number_phone="9204669750")
test.login_by_email(email="zazc256@gmail.com")
