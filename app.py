import os
from twilio.rest import Client

title = os.getenv("INPUT_IUTITLE")
body=os.getenv("INPUT_IU_BODY")
comment=os.getenv("INPUT_IU_COM")
num = os.getenv("INPUT_IUNUM")
name = os.getenv('GITHUB_ACTOR')
event = os.getenv("GITHUB_EVENT_NAME")
repo = os.getenv("GITHUB_REPOSITORY")
action = os.getenv('INPUT_EVENT_ACTION')
stars  = os.getenv("INPUT_STARGAZERS")
forks  = os.getenv("INPUT_FORKERS")
From = os.getenv('INPUT_FROM')
To = os.getenv('INPUT_TO')
account_sid=os.getenv('INPUT_TWILIO_ACCOUNT_SID')
authtoken=os.getenv('INPUT_TWILIO_AUTH')

if title is None:
    title = os.getenv('INPUT_PRTITLE')
if num is None:
    num = os.getenv('INPUT_PRNUM')
if body is None:
    body=os.getenv("INPUT_PR_BODY")


# ---------- Checking for responses ---------------

if event == "pull_request":
    repo_url = f'https://github.com/{repo}/pulls/{num}'
    if action == "opened":
        response = f'A new Pull request *{title}* *#{num}* has been opened in *{repo}* by *{name}*  \n\n {repo_url}'
        
    elif action == 'closed':
        response = f'The Pull request *{title}* *#{num}* on *{repo}* has been closed by *{name}*, \n\n {repo_url}'

    else:
        response = f'A new {action} event was triggered on the PR *{title}* *#{num}* on *{repo}*  by *{name}*, \n\n {repo_url}'


elif event == 'issues':
    repo_url = f'https://github.com/{repo}/issues/{num}'
    if action == 'opened':
        response = f'A new Issue *{title}* *#{num}* has been opened in *{repo}* by *{name}* \n\n {repo_url}'
        
    elif action == 'closed':
        response = f'The Issue *{title}* *#{num}* on *{repo}* was closed by *{name}*, \n\n {repo_url}'
   
    elif action == 'reopened':
        response = f'The Issue *{title}* *#{num}* on *{repo}* was reopened by *{name}*, \n\n {repo_url}'


    else:
        response = f'A new {action}  on the issue *{title}* *#{num}* on *{repo}* was done  by *{name}*, \n\n {repo_url}'


elif event=='issue_comment':
    repo_url = f'https://github.com/{repo}/issues/{num}'
    response = f'*{name}* commented  _{comment}_ on issue *#{num}* of *{repo}*  \n\n {repo_url}'

elif event=='page_build':
    page_url='https://'+name+'.github.io/'+repo
    response = f'A new page build was triggered on the  on *{repo}*  by *{name}*, \n\n {page_url}'

elif event=='watch':
    repo_url = f'https://github.com/{repo}/'
    response=f'*{name}* starred/forked your repo *{repo}* \n *Stars:{stars}* \n *Forks:{forks}* \n\n{repo_url}'



else:
    repo_url = f'https://github.com/{repo}'
    response = f'A new *{event}* has been made in *{repo}* by *{name}*, \n\n {repo_url}'


#creating twilio client

From='whatsapp:'+From
To='whatsapp:'+To
client=Client()
message = client.messages \
    .create(
         from_=From,
         body=response,
         to=To
     )
print('Message Sent')
