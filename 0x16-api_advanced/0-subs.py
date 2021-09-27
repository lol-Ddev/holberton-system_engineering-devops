#!/usr/bin/python3
"""
    Write a function that queries the Reddit API
    and returns the number of subscribers
"""

import requests

def number_of_subscribers(subreddit):
    """ return number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0:APIrequest:v1.2.3 (by u/esneidergrvc)"
    }
    response = requests.get(url, headers=headers).json()
    try:
        return (response['data']['subscribers'])
    except:
        return 0
