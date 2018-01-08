from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import gitcoinbotactions.githubActions as gitcoinBot
import json

def index(request):
    return HttpResponse("Hello, world. You're at the gitcoin bot index.")

@csrf_exempt
def payload(request):
    # parse request.body bytes into json and parse out relevant info

    if request.method == "POST":
        requestJSON = json.loads(request.body.decode('utf8'))

        if requestJSON['action'] == 'deleted':
            pass
        else:
            issueURL = requestJSON['comment']['url']
            owner = requestJSON['repository']['owner']['login']
            repo = requestJSON['repository']['name']
            comment_id = requestJSON['comment']['id']
            commentText = requestJSON['comment']['body']
            print("Going to try and react with a heart")
            gitcoinBot.post_issue_comment_reaction(owner, repo, comment_id, 'heart')

            return True