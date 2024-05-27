from onlinesimru import FreeNumbersService, RentNumbersService, ProxyService, UserService, NumbersService

from data.config import KEY_SIM_API


class Number:
    def __init__(self):
        self.numbers = NumbersService(apikey=KEY_SIM_API)
        self.tzid = self.numbers.get('ozon', number=True)
        self.tz = int(self.tzid.get('tzid'))

    def get_number(self) -> str:
        """
        Get number phone
        :return: number phone
        """
        return self.tzid.get('number')[2:]

    def get_code(self) -> str:
        """
        Get wait code
        :return: code
        """
        code = self.numbers.wait_code(self.tz)
        return code
