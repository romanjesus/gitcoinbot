'''
Methods for interacting with the Github API
'''
from django.conf import settings

import json
import requests
import re

_auth = (settings.GITHUB_API_USER, settings.GITHUB_API_TOKEN)

headers = {
    'Accept': 'application/vnd.github.squirrel-girl-preview'
}

v3headers = {
    'Accept': 'application/vnd.github.v3.text-match+json'
}

def construct_help_text():
    help_text_response = "I am @{}, a bot that facilitaes gitcoin bounties.\n".format(settings.GITHUB_API_USER) + \
        "\n" +\
        "<hr>" +\
        "Here are the commands I understand:\n" +\
        "\n" +\
        " * `bounty <amount> ETH` -- receive link to gitcoin.co form to create bounty.\n" +\
        " * `claim` -- receive link to gitcoin.co to claim bounty.\n" +\
        " * `approve` -- receive link to gitcoin.co to approve bounty.\n" +\
        " * `tip <user> <amount> ETH` -- receive link to complete tippping another github user *<amount>* ETH.\n" +\
        " * `help` -- displays a help menu\n" +\
        "\n" +\
        "<br>" +\
        "Learn more at: [https://gitcoin.co](https://gitcoin.co)\n" +\
        ":zap::heart:, {}\n".format("@" + settings.GITHUB_API_USER) +\
        "\n"
    return help_text_response


def post_issue_comment(owner, repo, issue_num, comment):
    url = 'https://api.github.com/repos/{}/{}/issues/{}/comments'.format(
        owner, repo, issue_num)
    body = {
        'body': comment,
    }
    response = requests.post(url, data=json.dumps(body), auth=_auth)
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

def determine_response(owner, repo, comment_id, comment_text, issue_id):
    help_regex = '@?[Gg]itcoinbot\s[Hh]elp'
    bounty_regex = '@?[Gg]itcoinbot\s[Bb]ounty\s\d*\.?(\d+\s?)(ETH|eth)'
    claim_regex = '@?[Gg]itcoinbot\s[Cc]laim'
    approve_regex = '@?[Gg]itcoinbot\s[Aa]pprove'
    tip_regex = '@?[Gg]itcoinbot\s[Tt]ip\s@\w*\s\d*\.?(\d+\s?)(ETH|eth)'

    if re.match(help_regex, comment_text) is not None:
        post_issue_comment_reaction(owner, repo, comment_id, '+1')
        post_issue_comment(owner, repo, issue_id, construct_help_text())
    elif re.match(bounty_regex, comment_text) is not None:
        pass
    elif re.match(claim_regex, comment_text) is not None:
        pass
    elif re.match(approve_regex, comment_text) is not None:
        pass
    elif re.match(tip_regex, comment_text) is not None:
        pass
    else:
        # Sorry I did not understand that response
        pass

