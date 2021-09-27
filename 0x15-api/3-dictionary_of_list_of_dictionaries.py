#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com'
    with requests.Session() as s:
        employee = s.get('{}/users/'.format(api_url)).json()
        to_dos = s.get('{}/todos/'.format(api_url)).json()

        todo_list = []
        completed_tasks = 0
        json_file = {}
        for task in to_dos:
            try:
                json_file[task.get('userId')].append(
                    {'username': employee[task.get('userId') - 1].
                     get('username'),
                     'task': task.get('title'),
                     'completed': task.get('completed')})
            except:
                json_file[task.get('userId')] = []
                json_file[task.get('userId')].append(
                    {'username': employee[task.get('userId') - 1].
                     get('username'),
                     'task': task.get('title'),
                     'completed': task.get('completed')})

        with open('todo_all_employees.json', 'w') as f:
            json.dump(json_file, f)
