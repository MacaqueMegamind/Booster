from selenium.webdriver.support.wait import WebDriverWait
from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time

from backend.online_sim.number import Number
from data.xpath_config import XPATHRegistration


class Registration:
    def __init__(self, time_delay: int):
        self.driver = Driver()
        self.time_delay = time_delay

    def registration_by_phone(self, number: Number):
        """
        Registration by number phone and input code
        :param number: Number object
        :return:
        """
        self.driver.get(XPATHRegistration.StartPage)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, XPATHRegistration.AUTH_FORM)))
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((By.XPATH, XPATHRegistration.AUTH_FORM)))
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_FORM).send_keys(number.get_number())
        auth = self.driver.find_element(By.XPATH, XPATHRegistration.AUTH_FORM)
        auth.find_element(By.XPATH, XPATHRegistration.SIGN_IN_BUTTON).click()
        time.sleep(self.time_delay)
        auth.find_element(By.XPATH, XPATHRegistration.ADVERTISEMENT_BUTTON).click()
        auth.find_element(By.XPATH, XPATHRegistration.AGREEMENT_BUTTON).click()
        WebDriverWait(self.driver, 70).until(
            ec.visibility_of_element_located((By.XPATH, XPATHRegistration.INPUT_CODE_FORM_BY_PHONE)))
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_CODE_FORM_BY_PHONE).click()
        code = number.get_code()
        print(code)
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_CODE_FORM).send_keys(code)
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
        time.sleep(self.time_delay)
        self.driver.find_element(By.XPATH, XPATHRegistration.ADD_EMAIL_FORM).send_keys(email)
        time.sleep(self.time_delay)
        self.driver.find_element(By.XPATH, XPATHRegistration.GET_CODE_BY_EMAIL_BUTTON).click()
        time.sleep(self.time_delay)
        self.driver.find_element(By.XPATH, XPATHRegistration.INPUT_CODE_FORM_BY_EMAIL).send_keys(int(input()))

        if input():
            self.driver.quit()


test = Registration(time_delay=3)
num = Number()
test.registration_by_phone(number=num)
# test.add_email(email="vanekforest@yandex.ru")
