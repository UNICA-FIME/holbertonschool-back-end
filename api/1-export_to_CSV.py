#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
"""
import csv
import json
from sys import argv
from urllib.request import urlopen


def for_api():
    ''' obtener informacion de api '''
    url = "https://jsonplaceholder.typicode.com/users/{}".format(int(argv[1]))
    req = urlopen(url).read().decode("utf-8")
    json_user = json.loads(req)
    USER_ID = json_user['id']
    USERNAME = json_user['name']

    url_todos = "https://jsonplaceholder.typicode.com\
/users/{}/todos/".format(int(argv[1]))
    req_todos = urlopen(url_todos).read().decode("utf-8")
    json_todos = json.loads(req_todos)
    with open(f'{argv[1]}.csv', 'w', encoding='UTF8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for item in json_todos:
            TASK_COMPLETED_STATUS = item['completed']
            TASK_TITLE = item['title']
            data = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
            writer.writerow(data)


if __name__ == "__main__":
    for_api()
