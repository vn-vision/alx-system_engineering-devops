#!/usr/bin/python3
''' make an api call to get the number of subscribers in a subreddit'''

import requests


def number_of_subscribers(subreddit):
    # get the number of subscribers
    # Set custom user-agent to avoid errors related to too many requests

    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # get response from endpoint, set headers, restrict redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        all_data = response.json()
        return all_data['data']['subscribers']
    except requests.RequestException:
        return 0
