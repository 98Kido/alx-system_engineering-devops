#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyBot/0.1 (by /u/Fickle-Elk-8988)'
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error: Status code {response.status_code}")
            return 0
    
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return 0

