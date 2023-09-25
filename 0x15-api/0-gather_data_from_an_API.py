#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com
returns information about employee's todo list progress
"""

from sys import argv
import requests


def fetch_user_data(user_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        user_response = requests.get(user_url, verify=False)
        todo_response = requests.get(todo_url, verify=False)

        user_data = user_response.json()
        todo_data = todo_response.json()

        return user_data, todo_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


def main():
    if len(argv) != 2:
        print("Usage:python script.py <employee_id>")
        return

    user_id = argv[1]
    user_data, todo_data = fetch_user_data(user_id)

    if user_data is None or todo_data is None:
        return

    completed_tasks = [
            task['title'] for task in todo_data if task.get('completed')
        ]
    total_tasks = len(todo_data)

    print(f"Employee {user_data['name']} is done with tasks({len(
            completed_tasks)}/{total_tasks}): ")
    print("\n".join(f"\t{task}" for task in completed_tasks))


if __name__ == '__main__':
    main()
