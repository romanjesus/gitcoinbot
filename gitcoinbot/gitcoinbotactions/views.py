from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import gitcoinbotactions.githubActions as gitcoinBot
import json

def index(request):
    return HttpResponse("Hello, world. You're at the gitcoin bot index.")

@csrf_exempt
def payload(request):
    # parse request.body bytes into json and parse out relevant info and
    # respond with appropriate message

    if request.method == "POST":
        requestJSON = json.loads(request.body.decode('utf8'))

        if requestJSON['action'] == 'deleted':
            # Gitcoinbot should not process these actions
            return HttpResponse(status=204)
        else:
            issueURL = requestJSON['comment']['url']
            owner = requestJSON['repository']['owner']['login']
            repo = requestJSON['repository']['name']
            comment_id = requestJSON['comment']['id']
            comment_text = requestJSON['comment']['body']
            issue_id = requestJSON['issue']['number']

            gitcoinBot.determine_response(owner, repo, comment_id,
                                          comment_text, issue_id)

            return HttpResponse('Gitcoinbot Responded')
