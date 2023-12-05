import pytest
import requests

class TestFirstApi:
    names = [('Vit'), ('Ars'), ('123'), ("")]

    @pytest.mark.parametrize('name', names)
    def test1(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        name = 'vit'
        data = {'name': name}

        resp = requests.get(url, params=data)

        assert resp.status_code == 200, 'wrong response code'

        resp_dict = resp.json()
        assert 'answer' in resp_dict, 'no field answer'

        if len(name) == 0:
            exp_resp_text = f'Hello, someone'
        else:
            exp_resp_text = f'Hello, {name}'
        act_resp_text = resp_dict['answer']
        assert act_resp_text == exp_resp_text, 'actual text in response is not correct'

