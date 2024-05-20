#!/usr/bin/python3
''' fetch data provided the id '''
import requests
import sys

if __name__ == "__main__":
    ''' not importable '''
    url = "https://jsonplaceholder.typicode.com/"

    try:
        id = sys.argv[1]
    except IndexError:
        print("Requires an ID")
        exit(1)

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    finished = [t.get('title') for t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(finished), len(todos)))
    [print("\t {}".format(c)) for c in finished]
