#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API.
    - If not a valid subreddit, return 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    headers = {"User-Agent": "MyApp/0.0.1"}

    try:
        req = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            headers=headers,
            allow_redirects=False  # Prevents auto-following redirects
        )

        if req.status_code == 200:
            return req.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
