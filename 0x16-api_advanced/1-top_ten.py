#!/usr/bin/python3
''' Query the Reddit API and print the titles of the first 10 hot posts
in a given subreddit'''

import requests


def top_ten(subreddit):
    # get subreddit, print None if not found
    # avoid redirects

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-app.0.0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            hot = response.json()

            # get the list with posts
            htChild = hot['data']['children']
            # get the top ten
            htData = htChild[:9]

            # loop through the list
            for ttl in htData:
                titles = ttl['data']['title']
                return titles

        elif response.status_code == 404:
            return 0
        else:
            return 0

    except requests.RequestException as e:
        print("Error: {}".format(e))


top_ten('programming')
