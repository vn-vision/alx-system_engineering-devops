#!/usr/bin/python3
''' recursive function that prints a sorted count of given keywords '''

import time
import requests
import re


def count_words(subreddit, word_list, word_count=None, after=None):
    ''' count number a word occurs  '''

    if word_count is None:
        word_count = {}

    if not word_list:
        return None

    # convert word list to lowercase and remove duplicates
    word_list = [word.lower() for word in word_list]
    word_list = list(set(word_list))

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "vn-vision/0.0.1"}
    params = {'show': 'all', 'after': after}

    if subreddit is None or not isinstance(subreddit, str):
        return None

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                word_count[word] = word_count.get(word, 0) + len(
                        re.findall(r'\b' + re.escape(word) + r'\b', title))

        after = data.get('after')
        if after:
            # delay for the api call
            time.sleep(1)
            return count_words(subreddit, word_list, word_count, after)
        else:
            if not word_count:
                return None

            # sort in descending order of value count,
            # alphabetical order of keys that start with similar word
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    # means it was present in title
                    print("{}: {}".format(word, count))
    except requests.RequestException:
        return None
