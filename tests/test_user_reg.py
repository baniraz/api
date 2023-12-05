# from datetime import datetime
# import requests

from lib.assertions import Assertion
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserRegister(BaseCase):
    # def setup_method(self):
    #     base_part = 'learnqa'
    #     domain = 'example.com'
    #     random = datetime.now().strftime('%m%d%Y%H%M%S')
    #     self.email = f'{base_part}{random}@{domain}'

    def test_create_user(self):
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': self.email
        # }

        data = self.prepare_reg_data()
        resp = MyRequests.post('/user', data=data)

        Assertion.assert_status_code(response=resp, exp_status=200)
        Assertion.assert_json_key(response=resp, id='id')

    def test_create_user_exist_email(self):
        email = 'vinkotov@example.com'
        # data = {
        #     'password': '123',
        #     'username': 'learnqa',
        #     'firstName': 'learnqa',
        #     'lastName': 'learnqa',
        #     'email': email
        # }

        data = self.prepare_reg_data(email=email)
        resp = MyRequests.post('/user', data=data)

        Assertion.assert_status_code(response=resp, exp_status=400)
        assert resp.content.decode('utf-8') == f"Users with email '{email}' already exists", f'error1'
