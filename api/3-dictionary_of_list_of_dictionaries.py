#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
On csv format.
"""
import csv
import json
from sys import argv
from urllib.request import urlopen


def for_api():
    ''' obtener informacion de api '''
    dict_json = {}
    dict_item = {}
    name = "todo_all_employees"
    url = "https://jsonplaceholder.typicode.com/users"
    req = urlopen(url).read().decode("utf-8")
    json_user = json.loads(req)

    url_todos = "https://jsonplaceholder.typicode.com/todos"
    req_todos = urlopen(url_todos).read().decode("utf-8")
    json_todos = json.loads(req_todos)

    with open('{}.json'.format(name), 'w', encoding='UTF8') as file:
        for item_1 in json_user:
            formato = []
            USER_ID = item_1['id']
            for item in json_todos:
                dict_item = {
                        "username": item_1["username"],
                        "task": item['title'],
                        "completed": item["completed"],
                        }
                formato.append(dict_item)
            dict_json[USER_ID] = formato
        json.dump(dict_json, file, indent=4)


if __name__ == "__main__":
    for_api()
