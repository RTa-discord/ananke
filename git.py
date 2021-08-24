import os
import json
import requests
from dotenv import load_dotenv
import json
import settings

def make_github_issue(title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
        data = r.json()
        print (json.dumps(data["number"]))
        return json.dumps(data["number"])
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)

def make_github_issue_comment(title, number, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues/%s/comments' % (REPO_OWNER, REPO_NAME, number)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue Comment {0:s}'.format(title))
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)


USERNAME = settings.USERNAME
PASSWORD = settings.PASSWORD

# The repository to add this issue to
REPO_OWNER = settings.REPO_OWNER
REPO_NAME = settings.REPO_NAME

TITLE = settings.TITLE
BODY = settings.BODY
LABELS = settings.LABELS

Number = make_github_issue(TITLE, body=BODY, labels=LABELS)
make_github_issue_comment(TITLE, Number, body=BODY, labels=LABELS)
