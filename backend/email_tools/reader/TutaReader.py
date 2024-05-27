from auto_chromedriver.driver import Driver
from selenium.webdriver import ChromeOptions
from email_tools.data.tuta_xpath_config import XPATH_Login, XPATH_VerifyMessage, XPATH_MessageList, XPATH_Message
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time


class TutaReader:
    def __init__(self, email: str, password: str, time_delay: int = 1, proxy: str = None):
        self.email = email
        self.password = password
        options = ChromeOptions()
        options.add_argument("--lang=en")
        if proxy:
            options.add_argument("--proxy-server=%s" % proxy)
        self.driver = Driver(options = options)
        self.time_delay = time_delay

    def login(self):
        self.driver.get(XPATH_Login.StartPage)

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, XPATH_Login.EMAIL_INPUT)))
        time.sleep(self.time_delay)

        self.driver.find_element(By.XPATH, XPATH_Login.EMAIL_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, XPATH_Login.PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, XPATH_Login.LOG_IN_BUTTON).click()

    def skip_verify_dialog(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, XPATH_VerifyMessage.DIALOG)))
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, XPATH_VerifyMessage.OK_BUTTON)))
        self.driver.find_element(By.XPATH, XPATH_VerifyMessage.OK_BUTTON).click()

    def get_list_of_messages(self) -> list[tuple[str, str]]:
        messages: list[tuple[str, str]] = []
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPATH_MessageList.MESSAGES_LIST)))
        number_of_messages = len(self.driver.find_elements(By.XPATH, XPATH_MessageList.MESSAGE))
        for index in range(1, number_of_messages + 1):
            XPATH_MESSAGE_WITH_INDEX = XPATH_MessageList.MESSAGE + f"[{index}]"
            message = self.driver.find_element(By.XPATH, XPATH_MESSAGE_WITH_INDEX)
            message_from = self.driver.find_element(By.XPATH,
                                                    XPATH_MESSAGE_WITH_INDEX + XPATH_MessageList.MESSAGE_FROM).text
            message_subject = self.driver.find_element(By.XPATH,
                                                       XPATH_MESSAGE_WITH_INDEX + XPATH_MessageList.MESSAGE_SUBJECT).text
            messages.append((message_from, message_subject))
        return messages

    def get_message(self, index: int):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPATH_MessageList.MESSAGES_LIST)))

        XPATH_MESSAGE_WITH_INDEX = XPATH_MessageList.MESSAGE + f"[{index}]"
        message = self.driver.find_element(By.XPATH, XPATH_MESSAGE_WITH_INDEX)
        message_from = self.driver.find_element(By.XPATH,
                                                XPATH_MESSAGE_WITH_INDEX + XPATH_MessageList.MESSAGE_FROM).text
        message_subject = self.driver.find_element(By.XPATH,
                                                   XPATH_MESSAGE_WITH_INDEX + XPATH_MessageList.MESSAGE_SUBJECT).text
        message.click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPATH_Message.MAIL_VIEWER)))
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, XPATH_Message.MESSAGE)))

        shadow_root = self.driver.find_element(By.XPATH, XPATH_Message.MESSAGE).shadow_root
        mail = shadow_root.find_element(By.CLASS_NAME, "messageReplySection")

        return message_from, message_subject, mail.text

    def get_last_message(self):
        return self.get_message(1)

    def quit(self):
        self.driver.quit()


if __name__ == "__main__":
    reader = TutaReader("huilockasosisochka@tutamail.com", "ALAT1375BY")
    reader.login()

    try:
        reader.skip_verify_dialog()
    except:
        pass

    messages = reader.get_list_of_messages()
    for message in messages:
        print(message)
    message1 = reader.get_message(1)
    print(message1)

    print("\nCODE")
    from email_tools.wrapper.codes import get_code
    print(get_code(reader.get_last_message()[2]))


    if input():
        reader.quit()
