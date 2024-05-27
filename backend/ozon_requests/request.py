import json
from auto_chromedriver.driver import Driver
from seleniumrequests.request import RequestsSessionMixin


class CustomRequestDriver(RequestsSessionMixin, Driver):
    def __init__(self, fake=False):
        super().__init__(fake=fake)


class Request:
    def __init__(self, cookies: list[dict]):
        self.cookies = cookies
        self.driver = CustomRequestDriver()

    def web(self):
        file = open("headers/web.json")
        settings = json.load(file)
        file.close()

        headers = settings['headers']
        headers["Cookie"] = json.dumps(self.cookies)

        response = self.driver.request("POST",
                                       "https://xapi.ozon.ru/perf-metrics-collector/v4/rum/bx/web",
                                       headers=headers
                                       )
        return response.headers

    def multi(self):
        file = open("headers/multi.json")
        settings = json.load(file)
        file.close()

        headers = settings['headers']
        headers["Cookie"] = json.dumps(self.cookies)

        response = self.driver.request("POST",
                                       "https://xapi.ozon.ru/dlte/multi",
                                       headers=headers
                                       )
        return response.headers

    def ozon_request(self):
        file = open("headers/ozon.json")
        settings = json.load(file)
        file.close()

        headers = settings['headers']
        headers["Cookie"] = json.dumps(self.cookies)

        response = self.driver.request("GET",
                                       "https://xapi.ozon.ru/",
                                       headers=headers
                                       )
        return response.headers
