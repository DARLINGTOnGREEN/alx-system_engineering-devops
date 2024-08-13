#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests
import time

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API.
    - If not a valid subreddit, return 0.
    """
    # Validate the subreddit input
    if not subreddit or not isinstance(subreddit, str):
        return 0
    
    # Set a more descriptive User-Agent header
    headers = {"User-Agent": "MyApp/0.0.1"}

    try:
        # Simple delay to avoid hitting rate limits (if needed)
        time.sleep(1)
        
        # Make the API request
        req = requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            headers=headers,
        )

        # Check if the request was successful
        if req.status_code == 200:
            # Safely parse the JSON response
            return req.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except (requests.RequestException, ValueError):
        # Handle exceptions related to the request or JSON parsing
        return 0
