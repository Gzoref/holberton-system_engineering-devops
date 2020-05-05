#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
TODO list progress in JSON format.
'''

if __name__ == '__main__':
    import json
    import requests

    user = requests.get('https://jsonplaceholder.typicode.com/users')
    name = user.json()
    json_data = {}

    for user in name:
        username = user.get('username')
        user_id = str(user.get('id'))
        url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
        task = requests.get(url)
        task_data = task.json()

    json_dictionary = {}
    json_list = []

    for item in task_data:
        json_dictionary['task'] = item.get('title')
        json_dictionary['completed'] = item.get('completed')
        json_dictionary['username'] = username
        json_list.append(json_dictionary)
        json_dictionary = {}

    json_data[user_id] = json_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_data, json_file)
