from onlinesimru import FreeNumbersService, RentNumbersService, ProxyService, UserService, NumbersService

from backend.data.config import KEY_SIM_API


class Number:
    def __init__(self):
        self.numbers = NumbersService(apikey=KEY_SIM_API)
        self.num = self.numbers.get('ozon', number=True)

    def get_number(self) -> str:
        """
        Get number phone
        :return: number phone
        """
        return self.num.get('number')[2:]

    def get_code(self) -> str:
        """
        Get wait code
        :return: code
        """
        return self.numbers.wait_code(self.num)
