import json.decoder
from datetime import datetime

from requests import Response


class BaseCase:
    def get_cookie(self, resp: Response, cookie_name):
        assert cookie_name in resp.cookies, 'error1'
        return resp.cookies[cookie_name]

    def get_header(self, resp: Response, headers_name):
        assert headers_name in resp.headers, 'error2'
        return resp.headers[headers_name]

    def get_json_value(self, resp: Response, name):
        try:
            resp_dict = resp.json()
        except json.decoder.JSONDecodeError:
            assert False, 'error3'

        assert name in resp_dict, f'error4 {name}'

        return resp_dict[name]

    def prepare_reg_data(self, email=None):
        if email is None:
            base_part = 'learnqa'
            domain = 'example.com'
            random = datetime.now().strftime('%m%d%Y%H%M%S')
            email = f'{base_part}{random}@{domain}'

        return {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }