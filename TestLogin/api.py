import json

import requests


class Login:
    """Апи библиотека"""

    def __init__(self):
        self.base_url = "https://virtserver.swaggerhub.com/roga88/bunker/1.0.0"

    def post_api_login(self, login: str, password: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя, найденного по указанным логину и паролю"""

        data = {
            "login": login,
            "password": password
        }
        res = requests.post(self.base_url+'/login', data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_api_login(self, login: str, password: str) -> json:
        """Метод для деструктивного тестирования"""

        data = {
            "login": login,
            "password": password
        }
        res = requests.put(self.base_url+'/login', data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_login_content_type(self, login: str, password: str) -> json:
        """Метод для деструктивного тестирования"""

        headers = {
            "Content-Type": "application/xml"
        }
        data = {
            "login": login,
            "password": password
        }
        res = requests.post(self.base_url+'/login', headers=headers, data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result