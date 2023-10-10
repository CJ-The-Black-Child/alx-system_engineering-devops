#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the title of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    This returns a list of containing titles of all hot
    articles on a subreddit.
    """
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    headers = {
        "User-Agent": "linux: 0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 100}

    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
        )

    """
    Check for invalid subreddit or if no results are found
    """
    if response.status_code == 404:
        return None

    data = response.json().get("data")
    hot_list.extend(post["data"]["title"] for post in data["children"])

    """
    if there are more pages, recursively call the function
    """
    if data["after"] is not None:
        return recurse(subreddit, hot_list)

    return hot_list
