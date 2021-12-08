# -*- coding: utf-8 -*-
"""добавить файл test_add_pet, в котором добавляем 2 вспомогательные функции: post_pet и delete_pet
далее создаем тестовую функцию test_positive, внутри тестовой функции выполняем следующие шаги:
a. Предусловие. сгенерировать данные для запроса POST/v2/pet, а именно: id, category, name, photoUrls, tags, status
b. Выполнение запроса. вызвать нашу вспомогательную функцию post_pet которую создали ранее
в параметрах передать значении id, category, name, photoUrls, tags, status
с. Постусловие. удалить ранее созданный объект Pet,
для этого вызываем вспомогательную функцию delete_pet в параметрах функции передаем pet_id
d. выполнить проверки через assert для response ручки POST/v2/pet: статус код == 200 значение status в запросе
и в ответе должны совпадать значение name в запросе и в ответе должны совпадать"""
import requests
from random import *


def post_pet(id, category, name, photoUrls, tags, status):
    api_method = "v2/pet"
    url = "https://petstore.swagger.io/" + api_method

    header = {"Accept": "application/json"}

    req_dict = {
        "id": id,
        "category": category,
        "name": name,
        "photoUrls":
            photoUrls,
        "tags": tags,
        "status": status
    }

    response = requests.request("POST", url, headers=header, json=req_dict)
    resp_dict = response.json()
    print(resp_dict)
    return response.status_code, resp_dict


def delete_pet(id):
    api_method = "v2/pet"
    url = "https://petstore.swagger.io/" + api_method + "/" + f'{id}'

    header = {"Accept": "application/json"}

    response = requests.request("DELETE", url, headers=header)
    return response


def test_positive():
    pet_id = randint(10, 99)
    category = {
        "id": randint(10, 99),
        "name": "anypet"
    }
    name = "Sharick"
    photoUrls = ["anyurlToImage"]
    tags = [{
        "id": randint(10, 99),
        "name": "tg"
    }]
    status = choice(["available", "pending", "sold"])

    pet = post_pet(pet_id, category, name, photoUrls, tags, status)
    delete_pet(pet_id)
    assert pet[0] == 200
    assert pet[1]["name"] == 'Sharick'
