#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her
TODO list progress in JSON format.
'''

if __name__ == '__main__':
    import json
    import requests

    user = requests.get('https://jsonplaceholder.typicode.com/users')
    name = len(user.json())

    json_return = {}

    for USER_ID in range(1, name):

        user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                            format(USER_ID))
        name = user.json()
        username = name.get('username')

        r = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.
                         format(USER_ID))

        todos = r.json()

        json_list = []
        json_dictionary = {}

        for item in todos:
            json_dictionary['task'] = item.get('title')
            json_dictionary['completed'] = item.get('completed')
            json_dictionary['username'] = username
            json_list.append(json_dictionary)

        json_return[USER_ID] = json_list

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_return, json_file)
