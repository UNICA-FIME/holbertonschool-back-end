#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
from sys import argv
from urllib.request import urlopen


def for_api():
    EMPLOYEE_NAME = None
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    url = "https://jsonplaceholder.typicode.com/users/{}".format(int(argv[1]))
    req = urlopen(url).read().decode("utf-8")
    json_user = json.loads(req)
    EMPLOYEE_NAME = json_user['name']
    url_todos = "https://jsonplaceholder.typicode.com\
/users/{}/todos".format(int(argv[1]))
    req_todos = urlopen(url_todos).read().decode("utf-8")
    json_todos = json.loads(req_todos)
    TOTAL_NUMBER_OF_TASKS = len(json_todos)
    url_todos_task = "https://jsonplaceholder.typicode.com\
/users/{}/todos/?completed=true".format(int(argv[1]))
    req_todos_task = urlopen(url_todos_task).read().decode("utf-8")
    json_todos_task = json.loads(req_todos_task)
    NUMBER_OF_DONE_TASKS = len(json_todos_task)
    print("Employee {} is done with tasks({}/{}):".format(
                                                      EMPLOYEE_NAME,
                                                      NUMBER_OF_DONE_TASKS,
                                                      TOTAL_NUMBER_OF_TASKS))
    for item in json_todos_task:
        print("\t {}".format(item.get("title")))


if __name__ == "__main__":
    for_api()
