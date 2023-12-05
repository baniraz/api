import pytest
import requests

from lib.assertions import Assertion
from lib.base_case import BaseCase


class TestUserAuth(BaseCase):
    params = [('no_cookie'), ('no_token')]

    def setup_method(self):
        data = {'email': 'vinkotov@example.com',
                'password': '1234'}

        resp = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(resp, 'auth_sid')
        self.token = self.get_header(resp, 'x-csrf-token')
        self.user_id_from = self.get_json_value(resp, 'user_id')

    def test_user_auth(self):
        resp2 = requests.get('https://playground.learnqa.ru/api/user/auth',
                             headers={'x-csrf-token': self.token}, cookies={'auth_sid': self.auth_sid})

        Assertion.assert_json_value(resp2, name='user_id', exp_value=self.user_id_from, error_msg='error000')
        assert 'user_id' in resp2.json(), 'error4'
        user_id_from_check = resp2.json()['user_id']
        print(user_id_from_check)

        assert self.user_id_from == user_id_from_check, 'error5'

    @pytest.mark.parametrize('cond', params)
    def test_negative(self, cond):
        if cond == 'no_cookie':
            resp2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token': self.token})
        else:
            resp2 = requests.get('https://playground.learnqa.ru/api/user/auth', cookies={'auth_sid': self.auth_sid})

        Assertion.assert_json_value(response=resp2, name='user_id', exp_value=0, error_msg=f'user is autorized with {cond}')

