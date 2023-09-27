#!/usr/bin/python3
"""
0-gather_data_from_an_API.py
This script getches information about an employee's todo list progress
using the JSONPlaceholder API.

Usage:
    python 0-gather_data_from_an_API.py <employee_id>

Example:
    python 0-gather_data_from_an_API.py 1

It imports the 'requests' library to make HTTP requests to the API and
displays completed tasks for the specified employee.

Uses https://jsonplaceholder.typicode.com along with an employee Id to
returns information about employee's todo list progress

API Endpoint:
    https://jsonplaceholder.typicode.com
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get(
            "https://jsonplaceholder.typicode.com/users", verify=False).json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/todos", verify=False).json()
    for task in todo:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
