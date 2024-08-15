#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}

    try:
        req = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if req.status_code == 200:
            # Check if the response is JSON
            if 'application/json' in req.headers.get('Content-Type', ''):
                data = req.json()
                posts = data.get("data", {}).get("children", [])
                
                if posts:
                    for post in posts:
                        title = post.get("data", {}).get("title", "No title available")
                        print(title)
                else:
                    print("No posts found.")
            else:
                print(None)
        else:
            print(None)
    except requests.exceptions.RequestException as e:
        print(None)
    except ValueError:
        print(None)

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        top_ten(sys.argv[1])
    else:
        print("Usage: ./1-main.py <subreddit>")
