#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit. If an invalid subreddit is provided, it returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, it returns 0.
    """
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
