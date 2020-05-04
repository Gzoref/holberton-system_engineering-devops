#!/usr/bin/python3
'''
For a given employee ID, returns information about his/her TODO list progress.
'''

if __name__ == '__main__':
    import requests
    import sys

    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1])).json()
    EMPLOYEE_NAME = req.get("name")
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                       format(sys.argv[1])).json()
    for item in req:
        if item.get('completed') is True:
            TASK_TITLE.append(item.get('title'))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(req)

    print('Employee {} is done with tasks({}/{}):'.
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for title in TASK_TITLE:
        print('\t {}'.format(title))
