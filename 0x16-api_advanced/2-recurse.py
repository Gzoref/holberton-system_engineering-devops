#!/usr/bin/python3
'''
Recursive function that queries the Reddit API
and returns a list containing the
titles of all hot articles for a given subreddit.
'''


def recurse(subreddit, hot_list=[], after=None, counter=0):
    '''
    Recursivly return list count
    of hot articles
    '''

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = 'reddit_user'
    headers = {'User-Agent': user_agent}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        return None
