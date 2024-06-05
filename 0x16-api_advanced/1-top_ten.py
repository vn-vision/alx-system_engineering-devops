#!/usr/bin/python3
''' Query the Reddit API and print the titles of the first 10 hot posts
in a given subreddit'''

import requests


def top_ten(subreddit):
    # get subreddit, print None if not found
    # avoid redirects

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my-app.0.0.1"}

    if subreddit is None or not isinstance(subreddit, str):
        return None
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)

        hot = response.json()

        # get the list with posts
        htChild = hot['data']['children']
        # get the top ten
        htData = htChild[:9]

        # loop through the list
        for ttl in htData:
            titles = ttl['data']['title']
            print(titles)

    except requests.RequestException:
        return None
