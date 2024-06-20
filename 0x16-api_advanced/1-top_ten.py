#!/usr/bin/python3

import requests

"""
Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

Args:
    subreddit (str): The name of the subreddit to query.

Returns:
    None: If the subreddit is invalid or an error occurs, prints None.
"""

def top_ten(subreddit):
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    title = post['data']['title']
                    print(title)
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)

