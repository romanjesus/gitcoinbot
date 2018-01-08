'''
Methods for interacting with the Github API
'''
from django.conf import settings

import json
import requests


_auth = (settings.GITHUB_API_USER, settings.GITHUB_API_TOKEN)

headers = {
    'Accept': 'application/vnd.github.squirrel-girl-preview'
}

v3headers = {
    'Accept': 'application/vnd.github.v3.text-match+json'
}

def help():
    params = {
        'sort': 'created',
        'direction': 'desc',
    }
    url = 'https://api.github.com/repos/{}/{}/issues/comments'.format(
        'romanjesus', 'gitcoinbot')
    response = requests.get(url, auth=_auth, headers=v3headers, params=params)

    return response.json()


def post_issue_comment_reaction(owner, repo, comment_id, content):
    url = 'https://api.github.com/repos/{}/{}/issues/comments/{}/reactions'.format(
        owner, repo, comment_id)
    body = {
        'content': content,
    }
    response = requests.post(url, data=json.dumps(
        body), auth=_auth, headers=headers)
    print('reacting with a heart')
    print(response.json())
    return response.json()
