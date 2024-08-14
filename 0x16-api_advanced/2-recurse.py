#!/usr/bin/python3
"""
Module to query the Reddit API and return a list containing the titles of all hot articles
for a given subreddit using recursion. If no results are found, the function returns None.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to return a list of titles of all hot articles for
    a given subreddit. If no results are found, returns None.

    :param subreddit: The subreddit to query
    :param hot_list: List to store titles of hot articles
    :param after: Pagination parameter for the next set of results
    :return: List of titles or None if the subreddit is invalid or has no hot articles
    """
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}  # Pagination, max 100 per request

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            
            # Check if there is a next page (pagination)
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list if hot_list else None
        else:
            return None
    except requests.RequestException:
        return None
