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


import requests
from sys import argv


def fetch_user_data(user_id):
    """
    Fetches user and todo list data for a given user ID.

    Args:
        user_id (int): The ID of the employee for whom to fetch data.

    Returns:
        tuple: A tuple containing users data and todo list data as
                dictionaries

    Raises:
        requests.exceptions.RequestException: An error occurred while making
        HTTP requests to the JSONPlaceHolder API.
    """
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
    """
    Main function to fetch
    display employee's todo list progress
    """
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
