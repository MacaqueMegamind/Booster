import json
import datetime
import openpyxl


def parse_from_response(response: str) -> list[dict]:
    n = response.count("Set-Cookie")
    cookies = []
    for i in range(n):
        start = response.find("Set-Cookie") + 14
        end = response.find("'", start)
        cookies.append(response[start:end])
        response = response[end:]

    for el in cookies:
        cookie_data = el.split(";")

        for i in range(len(cookie_data)):
            cookie_data[i] = cookie_data[i].strip()

        cookie = {}
        first = True
        for data in cookie_data:
            if first:
                key, value = data.split("=")
                cookie['name'] = key
                cookie['value'] = value
                first = False
                continue

            if data == "secure":
                cookie['secure'] = True
                continue
            if data == "HttpOnly":
                cookie['httpOnly'] = True
                continue

            key, value = data.split("=")
            if key == "domain":
                cookie[key] = '.' + value
                continue
            if key == "expires":
                cookie[key] = datetime.datetime.strptime(value, "%a, %d %b %Y %H:%M:%S %Z").timestamp()
                continue
            cookie[key] = value
        cookies[cookies.index(el)] = cookie
    return cookies


def parse_from_xlsx(xlsx_path, json_path):
    wb = openpyxl.load_workbook(xlsx_path)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    print(data)
    tags = ['name', 'value', 'domain', 'path', 'expires', 'size', 'httpOnly', 'secure', 'session', 'sameSite']
    file = open(json_path, 'w')
    obj = []
    for el in data:
        cur_obj = {}
        for i in range(len(el)):
            if tags[i] == 'expires':
                val = ""
                if el[i] == "Session":
                    val = "Session"
                else:
                    val = datetime.datetime.strptime(str(el[i]), '%Y-%m-%dT%H:%M:%S.%fZ').timestamp()
                cur_obj[tags[i]] = val
            elif tags[i] == 'httpOnly' or tags[i] == 'secure' or tags[i] == 'session':
                cur_obj[tags[i]] = str(bool(el[i])).lower()
            else:
                cur_obj[tags[i]] = el[i]
        obj.append(cur_obj)

    file.write(json.dumps(obj))


if __name__ == '__main__':
    pass
    # ls = parse_from_response("{'Server': 'nginx', 'Date': 'Thu, 23 May 2024 15:35:57 GMT', 'Content-Type': 'application/json', 'Content-Length': '266', 'Connection': 'keep-alive', 'Access-Control-Allow-Credentials': 'true', 'Access-Control-Allow-Origin': 'https://www.ozon.ru', 'Access-Control-Expose-Headers': 'X-O3-Trace-Id', 'Vary': 'Origin', 'x-o3-trace-id': '401cb8b4d9484a05', 'Set-Cookie': 'abt_data=a430d61b07c4304eba61eb1de16fef51:a593b3d47a27e21ba7369181b455d51d2b79204e588eb5c2bbdbeae61f30a359020664d74df6e17d49b5955208e9c54bf80c00963ae9678409f6a049826182da516219f272080dbd8794b669cd6c06152ddd4fa8e5bfed0e23462630bbb079b4346b681e84d06315aa0838882beabd94b8aa83de3c83651d21c9efa6cf150521d830b605e0c1a2bc6705e642f3b088167389f0acf3246d077a9dfc21bfe6abbcbd9c902fedb71243e6339982b73f84c9; expires=Fri, 23 May 2025 15:35:57 GMT; domain=ozon.ru; path=/; HttpOnly; secure; SameSite=Lax', 'Set-Cookie': '_ect=alal; expires=Fri, 23 May 2025 15:35:57 GMT; domain=ozon.ru; path=/; HttpOnly; secure; SameSite=Lax'}")
    # print(ls)
