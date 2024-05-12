from selenium.webdriver.support.wait import WebDriverWait
from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

from data.xpath_config import XPATHRegistration


class Registration:
    def __init__(self, time_delay: int):
        self.driver = Driver()
        self.time_delay = time_delay

    def registration_by_phone(self, number_phone: str):
        """
        Registration by number phone and input code
        :param number_phone: number phone
        :return:
        """
        self.driver.get(XPATHRegistration.StartPage)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, XPATHRegistration.AUTH_FORM)))
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_FORM).send_keys(number_phone)
        auth = self.driver.find_element(By.XPATH, XPATHRegistration.AUTH_FORM)
        auth.find_element(By.XPATH, XPATHRegistration.SIGN_IN_BUTTON).click()
        time.sleep(self.time_delay)
        auth.find_element(By.XPATH, XPATHRegistration.ADVERTISEMENT_BUTTON).click()
        auth.find_element(By.XPATH, XPATHRegistration.AGREEMENT_BUTTON).click()
        # здесь заменим потом int(input()) на получение кода с телефона
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_CODE_FORM).send_keys(int(input()))
        auth.find_element(By.XPATH, XPATHRegistration.REGISTRATION_BUTTON).click()

        if input():
            self.driver.quit()

    def add_email(self, email: str):
        """
        Add email
        :param email: email
        :return:
        """
        self.driver.get(XPATHRegistration.StartPage)
        time.sleep(self.time_delay)
        self.driver.find_element(By.XPATH, XPATHRegistration.ADD_EMAIL_BUTTON).click()

        if input():
            self.driver.quit()


test = Registration(time_delay=50)
test.add_email(email="zazc256@gmail.com")
