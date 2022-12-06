#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
On csv format.
"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    user_id = argv[1]

    user_url = '{}{}'.format(base_url, user_id)
    todo_url = '{}{}/todos'.format(base_url, user_id)

    user = get(user_url).json()
    all_tasks = get(todo_url).json()

    username = user.get('username')

    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in all_tasks:
            status = task.get("completed")
            title = task.get("title")
            data = [user_id, username, status, title]
            writer.writerow(data)
