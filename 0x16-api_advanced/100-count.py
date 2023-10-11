#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parse the title of all hot
articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_counts=None):
    """
    Prints count of specified words found in the hot
    artivles of a given reddit.

    Args:
        subreddot (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameters for the next page of the API results.
        word_counts (dict): A dictionary to store word counts.
    """
    if word_counts is None:
        word_counts = {word.lower(): 0 for word in word_list}

    user_agent = {'User-agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after} if after else {}

    response = requests.get(url, headers=user_agent, params=params)

    if response.status_code == 200:
        data = response.json()['data']
        aft = data['after']
        posts = data['children']

        for post in posts:
            title = post['data']['title'].lower()
            for word in title.split():
                word = word.rstrip('.!_')
                if word in word_counts:
                    word_counts[word] += 1

        if aft is not None:
            return count_words(subreddit, word_list, aft, word_counts)
        else:
            sorted_counts = sorted(
                word_counts.items(),
                key=lambda item: (-item[1], item[0].lower())
                )
            for word, count in sorted_counts:
                if count > 0:
                    print('{}: {}'.format(word, count))
