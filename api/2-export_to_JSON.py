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
    url = "https://jsonplaceholder.typicode.com/users/{}".format(int(argv[1]))
    req = urlopen(url).read().decode("utf-8")
    json_user = json.loads(req)
    USER_ID = int(argv[1])
    USERNAME = json_user['username']

    url_todos = "https://jsonplaceholder.typicode.com\
/users/{}/todos/".format(int(argv[1]))
    req_todos = urlopen(url_todos).read().decode("utf-8")
    json_todos = json.loads(req_todos)

    with open('{}.json'.format(int(argv[1])), 'w', encoding='UTF8') as file:
        dict_json = {
                USER_ID: []
                }
        for item in json_todos:
            dict_item = {
                    "username": USERNAME,
                    "task": item['title'],
                    "completed": item["completed"]
                    }
            dict_json[USER_ID].append(dict_item)
        json.dump(dict_json, file, indent=4)


if __name__ == "__main__":
    for_api()
