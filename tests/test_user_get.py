# import requests

from lib.assertions import Assertion
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):
    def test_get_user_not_auth(self):
        resp = MyRequests.get('/user/2')
        Assertion.assert_json_key(response=resp, id='username')
        Assertion.assert_json_not_key(response=resp, key='email')
        Assertion.assert_json_not_key(response=resp, key='firstName')
        Assertion.assert_json_not_key(response=resp, key='lastName')

    def test_get_the_same_user(self):
        data = {'email': 'vinkotov@example.com',
                'password': '1234'}

        resp = MyRequests.post('/user/login', data=data)

        auth_sid = self.get_cookie(resp, 'auth_sid')
        token = self.get_header(resp, 'x-csrf-token')
        user_id_from = self.get_json_value(resp, 'user_id')

        resp2 = MyRequests.get(f'/user/{user_id_from}',
                             headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        exp_fields = ['username', 'email', 'firstName', 'lastName']
        Assertion.assert_json_keys(response=resp2, keys=exp_fields)
