#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts
listed for a given subreddit. If an invalid subreddit is provided, it prints None.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, it prints None.
    """
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
