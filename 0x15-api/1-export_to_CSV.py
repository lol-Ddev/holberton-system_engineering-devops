#!/usr/bin/python3
"""
    a Python script that, using this REST API,
    for a given employee ID, returns information
    about his/her TODO list progress.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
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

        with open('{}.csv'.format(argv[1]), 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todo_list:
                writer.writerow([task['userId'], employee['username'],
                                task['completed'], task['title']])
