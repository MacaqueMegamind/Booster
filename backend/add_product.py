from data.xpath_config import XPATHAddProduct

from selenium.webdriver.support.wait import WebDriverWait

from auto_chromedriver.driver import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time


class AddProduct:
    def __init__(self, time_delay: int):
        self.driver = Driver()
        self.time_delay = time_delay

    def add_product_to_cart(self, product_link: str):
        """
        Adds product from link to cart
        :param product_link: Link to the product
        """
        driver = Driver()
        driver.get(product_link)
        time.sleep(self.time_delay)
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, XPATHAddProduct.XPATH_BUTTON_CART))
            )
            add_to_cart_button.click()
        finally:
            time.sleep(self.time_delay)
            driver.quit()

    def add_product_to_favorite(self, product_link: str):
        """
        Adds product from link to favorite
        :param product_link: Link to the product
        """
        driver = Driver()
        driver.get(product_link)
        time.sleep(self.time_delay)
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, XPATHAddProduct.XPATH_BUTTON_FAVORITE))
            )
            add_to_cart_button.click()
        finally:
            time.sleep(self.time_delay)
            driver.quit()


product_link = 'https://www.ozon.ru/product/futbolka-1381220957/?advert=ZcmILLXX4DcbpVJdaBPHSM8caLyXEt-oyYVbrvR0dDfkKK6kB5h7iklHuLNo8afqaUaU444KDoA83xBHV4u4vIBDboiHqHDOzTKMZFOGjER_Tk1zHEc3pTJf3s0nV2PuoqiqUNs9SY6PPuaqNVT73wXLgI41jO3MStvtBamcVeodud67lqkhuef6mSgaQA9uS-Ng2t9Q3Sk_79iiObsy8I4hHmVcOe-2Mk6q9ih8RrPH8Ks27Ex9MS7TD3LbU0xHDFZ4WgCKpocWIOf0dBPUo-o_4ieZvqd4zWCNuj2wQOlzAOpstEs7i-bK6Tv4OCKfTh8yQc5pPWM-Nbh7xIgCCm2gIkQlww&avtc=1&avte=2&avts=1712511396&clckid=b93b03d2&keywords=%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB%D0%BA%D0%B0+%D1%81%D0%BB%D0%B0%D0%B2%D0%B0+%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8'

# test = AddProduct(time_delay=3)
# test.add_product_to_cart(product_link=product_link)
# test.add_product_to_favorite(product_link=product_link)
