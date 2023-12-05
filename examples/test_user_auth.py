import pytest
import requests

class TestUserAuth:
    def test_user_auth(self):
        data = {'email':'vinkotov@example.com',
                'password':'1234'}

        resp = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert 'auth_sid' in resp.cookies, 'error1'
        assert 'x-csrf-token' in resp.headers, 'error2'
        assert 'user_id' in resp.json(), 'error3'

        auth_sid = resp.cookies.get('auth_sid')
        token = resp.headers.get('x-csrf-token')
        user_id_from = resp.json()['user_id']

        resp2 = requests.get('https://playground.learnqa.ru/api/user/auth',
                             headers={'x-csrf-token':token}, cookies={'auth_sid':auth_sid})

        assert 'user_id' in resp2.json(), 'error4'
        user_id_from_check = resp2.json()['user_id']
        assert user_id_from == user_id_from_check, 'error5'


    params = [('no_cookie'), ('no_token')]
    @pytest.mark.parametrize('cond', params)
    def test_negative(self, cond):
        data = {'email': 'vinkotov@example.com',
                'password': '1234'}

        resp = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert 'auth_sid' in resp.cookies, 'error1'
        assert 'x-csrf-token' in resp.headers, 'error2'
        assert 'user_id' in resp.json(), 'error3'

        auth_sid = resp.cookies.get('auth_sid')
        token = resp.headers.get('x-csrf-token')

        if cond == 'no_cookie':
            resp2 = requests.get('https://playground.learnqa.ru/api/user/auth', headers={'x-csrf-token':token})
        else:
            resp2 = requests.get('https://playground.learnqa.ru/api/user/auth', cookies = {'auth_sid': auth_sid})
        assert 'user_id' in resp2.json(), 'error1'
        user_id_from_check = resp2.json()['user_id']
        assert user_id_from_check == 0, 'error4'