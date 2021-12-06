# -*- coding: utf-8 -*-
"""автоматизировать ручку PUT/v2/user/{username}, для этого мы должны выполнить следующие шаги
 a. создать пользователя, данные для тело запроса генерируем рандомно:
  user_id, username, firstName, lastName, email, password, phone
  b. выполнить get запрос чтоб получить данные пользователя которого создалии ранее
  c. из response изменить значение в поле phone, выполнить put запрос
  d. еще раз выполнить get запрос чтоб получить новые значение ранее созданного пользователя
  e. выполнить проверку изменилось ли значение в поле phone"""

from random import randint
import requests


def post_user():
    api_method = "v2/user"
    url = "https://petstore.swagger.io/" + api_method

    header = {"Accept": "application/json"}

    req_dict = {

        "id": randint(100, 999),
        "username": "Alex",
        "firstName": "Alex",
        "lastName": "Vedin",
        "email": "test_alex@test.com",
        "password": "1234567890qwerty",
        "phone": "+79998889900",
        "userStatus": 0
    }

    requests.request("POST", url, headers=header, json=req_dict)
    return req_dict


def get_user():
    username = post_user()["username"]
    api_method = "v2/user/"
    url = "https://petstore.swagger.io/" + api_method + username
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.json()


def test_edit_user():
    before_edit = get_user()
    api_method = "v2/user/"
    edited_user = before_edit
    edited_user["phone"] = "+79996667745"
    url = "https://petstore.swagger.io/" + api_method + before_edit["username"]
    requests.put(url, json=edited_user)
    after_edit = get_user()
    print(before_edit["phone"])
    print(after_edit["phone"])
    assert before_edit["phone"] != after_edit["phone"]
