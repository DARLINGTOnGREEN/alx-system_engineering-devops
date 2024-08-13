#!/usr/bin/env python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""


import requests
import time


def number_of_subscribers(subreddit):

    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except KeyError as e:
            print(f"Error parsing JSON response: {e}")
            return 0
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found")
        return 0
    elif response.status_code == 429:
        print("Rate limit exceeded. Waiting 1 minute...")
        time.sleep(60)
        return number_of_subscribers(subreddit)  # retry after 1 minute
    else:
        print(f"Error {response.status_code}: {response.reason}")
        return 0
