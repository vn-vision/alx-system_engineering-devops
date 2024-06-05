#!/usr/bin/python3
''' recursive function that queries Reddit API
returns a list containing titles of all hot articles for a given
subreddit '''

import requests


def recurse(subreddit, hot_list=[], after=None):
    # the recurse function to return list of hot articles

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"show": 'all', "after": after}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    if data is None:
        return None

    for child in data['children']:
        hot_list.append(child['data']['title'])

    # check if theres a next page
    after = data.get('after')

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
