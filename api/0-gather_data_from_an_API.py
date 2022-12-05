#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
from urllib import request
import json
import sys

resp_user = request.urlopen('https://jsonplaceholder.typicode.com/users')
data_user = resp_user.read()
list_user = json.loads(data_user.decode("utf-8"))
dict_user = {}
for item in list_user:
    if item.get('id') == int(sys.argv[1]):
        dict_user.update(item)
EMPLOYEE_NAME = dict_user.get('name')
resp_todos = request.urlopen('https://jsonplaceholder.typicode.com/todos')
data_todos = resp_todos.read()
list_todos = json.loads(data_todos.decode("utf-8"))
count_true = 0
count_false = 0
list_task = []
for item in list_todos:
    if (item.get('userId') == int(sys.argv[1])
            and item.get('completed') is True):
        count_true += 1
        list_task.append(item['title'])
    if (item.get('userId') == int(sys.argv[1])
            and item.get('completed') is False):
        count_false += 1
NUMBER_OF_DONE_TASKS = count_true
TOTAL_NUMBER_OF_TASKS = count_true + count_false
print("Employee {} is done with tasks({}/{}):".format(
    EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
))
for item in list_task:
    print("\t{}".format(item))
