# -*- coding: utf-8 -*-
"""добавить файл test_get_wrong_username, выполнить негативный сценарии в параметризованной тестовой функции
test_negative, параметризовать по значению username со значениями 'wrong',
 'error' метод get_user должен вернуть нам 404 ошибку с сообщением User not found выполнить assertы на статус код,
 значение полей из response: type, message"""
import pytest
import requests


@pytest.mark.parametrize("username", ["wrong", "error"])
def test_negative(username):
    api_method = "v2/user/"
    url = "https://petstore.swagger.io/" + api_method + username
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    res_dic = response.json()
    assert response.status_code == 404
    assert res_dic["message"] == "User not found"
