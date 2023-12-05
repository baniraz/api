import json

from requests import Response


class Assertion:
    @staticmethod
    def assert_json_value(response: Response, name, exp_value, error_msg):
        try:
            resp_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, 'error1'

        assert name in resp_dict, 'error2'
        assert resp_dict[name] == exp_value, error_msg

    @staticmethod
    def assert_json_key(response: Response, id):
        try:
            resp_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, 'response is not in json format'

        assert id in resp_dict, f"response json doesn't have key'{id}'"

    @staticmethod
    def assert_json_keys(response: Response, keys: list):
        try:
            resp_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, 'response is not in json format'

        for key in keys:
            assert key in resp_dict, f"response json doesn't have key'{key}'"

    @staticmethod
    def assert_status_code(response: Response, exp_status):
        assert response.status_code == exp_status, f'expected {exp_status}, actual: {response.status_code}'

    @staticmethod
    def assert_json_not_key(response: Response, key):
        try:
            resp_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, 'response is not in json format'

        assert key not in resp_dict, f"response json shouldn't have key'{key}' but it is present"