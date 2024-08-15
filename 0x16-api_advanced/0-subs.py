#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""


import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function returns 0.
    """
    
    # Set a custom User-Agent to avoid errors related to Too Many Requests
    headers = {'User-Agent': 'My Reddit API Client'}
    
    # Construct the API request URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Send a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the request is successful (200 OK) and the subreddit exists
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Return the number of subscribers
        return data['data']['subscribers']
    else:
        # If the subreddit does not exist or the request fails, return 0
        return 0
