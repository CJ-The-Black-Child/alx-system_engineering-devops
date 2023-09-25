#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com
employee's todo list progress and exports it in JSON format
"""

import json
import requests


def fetch_user_data():
    try:
        users_response = requests.get(
                "https://jsonplaceholder.typicode.com/users", verify=False
                )
        todos_response = requests.get(
                "https://jsonplaceholder.typicode.com/todos", verify=False
                )

        if (users_response.status_code != 200 or
                todos_response.status_code != 200):
            print("Failed to fetch data. Check your internet \
                    connection or the API.")
            return None, None

        users = users_response.json()
        todos = todos_response.json()

        return users, todos

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


def create_todo_dict(users, todos):
    user_dict = {}

    for user in users:
        user_id = user['id']
        username = user['username']
        user_dict[user_id] = []

    for todo in todos:
        user_id = todo['userId']
        task_title = todo['title']
        completed = todo['completed']

        task_dict = {
                'username': users[user_id - 1]['username'],
                'task': task_title,
                'completed': completed
                }

        user_dict[user_id].append(task_dict)

    return user_dict


def export_to_json(todo_dict):
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(todo_dict, jsonfile, indent=4)


def main():
    users, todos = fetch_user_data()

    if users and todos:
        todo_dict = create_todo_dict(users, todos)
        export_to_json(todo_dict)
        print("Data exported to todo_all_employees.json")


if __name__ == '__main__':
    main()
