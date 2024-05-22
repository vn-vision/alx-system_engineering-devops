#!/usr/bin/python3
''' export data to JSON file given the ID '''

import json
import requests
import sys

if __name__ == "__main__":
    # limit importation
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonfile:
        json.dump({userId: [{"task": t.get("title"),
                             "completed": t.get("completed"),
                             "username": username}
                            for t in todos]}, jsonfile)
