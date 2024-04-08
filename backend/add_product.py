import asyncio

from selenium.webdriver.support.wait import WebDriverWait

from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


def add_product(product_link: str, xpath_to_add_cart_button: str):
    """
    Presses the selected button on the product card using xpath
    :param product_link: Link to the product
    :param xpath_to_add_cart_button: XPATH to the button
    """
    driver = Driver()
    driver.get(product_link)
    time.sleep(3)
    try:
        # Ожидание появления кнопки "Добавить в корзину" в течение 10 секунд
        add_to_cart_button = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, xpath_to_add_cart_button))
        )
        add_to_cart_button.click()
        # Действия после добавления в корзину
    finally:
        time.sleep(3)  # Пауза для демонстрации, что кнопка была нажата
        driver.quit()


product_link = 'https://www.ozon.ru/product/futbolka-1381220957/?advert=ZcmILLXX4DcbpVJdaBPHSM8caLyXEt-oyYVbrvR0dDfkKK6kB5h7iklHuLNo8afqaUaU444KDoA83xBHV4u4vIBDboiHqHDOzTKMZFOGjER_Tk1zHEc3pTJf3s0nV2PuoqiqUNs9SY6PPuaqNVT73wXLgI41jO3MStvtBamcVeodud67lqkhuef6mSgaQA9uS-Ng2t9Q3Sk_79iiObsy8I4hHmVcOe-2Mk6q9ih8RrPH8Ks27Ex9MS7TD3LbU0xHDFZ4WgCKpocWIOf0dBPUo-o_4ieZvqd4zWCNuj2wQOlzAOpstEs7i-bK6Tv4OCKfTh8yQc5pPWM-Nbh7xIgCCm2gIkQlww&avtc=1&avte=2&avts=1712511396&clckid=b93b03d2&keywords=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0+%D1%81%D0%BB%D0%B0%D0%B2%D0%B0+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'
xpath_button_cart = "//button[@class='y9j b200-a0 b200-b2 b200-a4']"
xpath_button_favorite = "//button[@class='z4j ag00-a0 ag00-a3']"
add_product(product_link=product_link, xpath_to_add_cart_button=xpath_button_cart)
add_product(product_link=product_link, xpath_to_add_cart_button=xpath_button_favorite)
