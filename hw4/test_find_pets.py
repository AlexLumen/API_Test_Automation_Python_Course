# -*- coding: utf-8 -*-
"""добавить файл test_find_pets.py в файле вспомогательная функция get_pets_by_status и
параметризованная тестовая функция test_positive со значением status ["available", "pending", "sold"]
Выполнить проверки на response через assert: a. статус код
b. проверить все ли элементы из response имеют status соответствующий из запроса"""
import pytest
import requests


def get_pets_by_status(status):
    api_method = "v2/pet/findByStatus"
    url = "https://petstore.swagger.io/" + api_method + "?" + "status=" + status
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    return response.status_code, response.json()


@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets(status):
    pets = get_pets_by_status(status)
    for item in pets[1]:
        assert item["status"] == status
    assert pets[0] == 200
