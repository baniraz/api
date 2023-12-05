# import requests

from lib.assertions import Assertion
from lib.base_case import BaseCase
from lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        reg_data = self.prepare_reg_data()
        resp = MyRequests.post('/user', data=reg_data)
        Assertion.assert_status_code(response=resp, exp_status=200)
        Assertion.assert_json_key(response=resp, id='id')

        email = reg_data['email']
        first_name = reg_data['firstName']
        password = reg_data['password']
        user_id = self.get_json_value(resp=resp, name='id')

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        resp2 = MyRequests.post('/user/login', data=login_data)

        auth_sid = self.get_cookie(resp2, 'auth_sid')
        token = self.get_header(resp2, 'x-csrf-token')

        # EDIT
        new_name = 'Changed Name'

        resp3 = MyRequests.put(f'/user/{user_id}',
                             headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid},
                             data={'firstName': new_name})

        Assertion.assert_status_code(response=resp3, exp_status=200)

        # GET
        resp4 = MyRequests.get(f'/user/{user_id}',
                             headers={'x-csrf-token': token}, cookies={'auth_sid': auth_sid})

        Assertion.assert_json_value(response=resp4, name='firstName', exp_value=new_name,
                                    error_msg='wrong name after edit')
