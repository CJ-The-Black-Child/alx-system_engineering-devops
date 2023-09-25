#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com
returns information about the employee's todo list progress and exports
it to CSV file
"""

import csv
import requests
from sys import argv


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


def export_to_csv(user_id, user_data, todo_data):
    if user_data is None or todo_data is None:
        return

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            taskwriter.writerow(
                    [user_id, user_data['username'],
                        task['completed'], task['title']])


def main():
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        return

    user_id = argv[1]
    user_data, todo_data = fetch_user_data(user_id)

    export_to_csv(user_id, user_data, todo_data)


if __name__ == '__main__':
    main()
