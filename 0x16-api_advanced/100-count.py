#!/usr/bin/python3
"""
Module to query the Reddit API and count occurrences of keywords in hot article titles
for a given subreddit using recursion. Results are sorted and printed in descending order
of count, and alphabetically for ties.
"""

import requests
import re
from collections import defaultdict

def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API to count the occurrences of keywords in hot article
    titles for a given subreddit. Results are printed in descending order of count and
    alphabetically for ties.

    :param subreddit: The subreddit to query
    :param word_list: List of keywords to count
    :param word_count: Dictionary to accumulate keyword counts
    :param after: Pagination parameter for the next set of results
    """
    if word_count is None:
        word_count = defaultdict(int)
    
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    # Create a regex pattern to match whole words only
                    pattern = re.compile(r'\b' + re.escape(word.lower()) + r'\b')
                    word_count[word.lower()] += len(pattern.findall(title))

            # Check if there is a next page (pagination)
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                # Print the results sorted by count (descending) and alphabetically (ascending)
                sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word} {count}")
        else:
            return None
    except requests.RequestException:
        return None
