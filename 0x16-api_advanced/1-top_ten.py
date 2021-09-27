#!/usr/bin/python3
"""
    Write a function that queries the Reddit API
    and returns the number of subscribers
"""

import requests


def top_ten(subreddit):
    """ return number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0:APIrequest:v1.2.3 (by u/esneidergrvc)"
    }

    response = requests.get(url, headers=headers).json()
    try:
        posts = response.get("data").get("children")
        for i in range(0, 10):
            print(posts[i].get("data").get("title"))
    except:
        print(None)
