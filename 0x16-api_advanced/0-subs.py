#!/usr/bin/python3
"""A function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers from the Reddit API"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-agent': 'Custom User-Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    
    try:
        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except ValueError:
        return 0  # Handles any JSON decode errors just in case
