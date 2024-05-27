from ozon_requests.request import Request
from ozon_requests.parser import parse_from_response
import json


def refresh(cookies: list[dict]) -> list[dict]:
    request = Request(cookies)
    response: list = [request.ozon_request(), request.web(), request.multi()]
    response_cookies: dict[str, dict] = {}
    for el in response:
        current_response_cookies: list[dict] = parse_from_response(str(el))
        for cookie in current_response_cookies:
            response_cookies[cookie['name']] = cookie

    result: list[dict] = []
    for response_cookie in response_cookies.values():
        result.append(response_cookie)
    return result


if __name__ == '__main__':
    file = open("../cookie_login/new_bot_api_cookies.json")
    print(refresh(json.load(file)))
