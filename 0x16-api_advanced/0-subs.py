#!/usr/bin/python3
''' make an api call to get the number of subscribers in a subreddit'''

import requests


def number_of_subscribers(subreddit):
    # get the number of subscribers
    # Set custom user-agent to avoid errors related to too many requests

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        # get response from endpoint, set headers, restrict redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            subreddit = response.json()
            return subreddit['data']['subscribers']
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
