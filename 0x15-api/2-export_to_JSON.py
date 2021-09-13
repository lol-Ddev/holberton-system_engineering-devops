#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import requests
from sys import argv
import json

user_id = argv[1]
api_url = 'https://jsonplaceholder.typicode.com'
with requests.Session() as s:
    employee = s.get('{}/users/{}'.format(api_url, user_id)).json()
    to_dos = s.get('{}/todos/'.format(api_url)).json()

    todo_list = []
    completed_tasks = 0
    for task in to_dos:
        if task['userId'] == int(user_id):
            todo_list.append(task)
            if task['completed'] is True:
                completed_tasks = completed_tasks + 1

    json_file = {user_id: []}
    for num, task in enumerate(todo_list):
        json_file[user_id].append({
            'task': todo_list[num].get('title'),
            'completed': todo_list[num].get('completed'),
            'username': employee.get('username')})

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(json_file, f)
