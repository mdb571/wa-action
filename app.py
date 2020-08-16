import os
from twilio.rest import Client

title = os.getenv("INPUT_IUTITLE")
num = os.getenv("INPUT_IUNUM")
name = os.getenv('GITHUB_ACTOR')
event = os.getenv("GITHUB_EVENT_NAME")
repo = os.getenv("GITHUB_REPOSITORY")
action = os.getenv('INPUT_EVENT_ACTION')
From = os.getenv('INPUT_FROM')
To = os.getenv('INPUT_TO')
account_sid=os.getenv('INPUT_TWILIO_ACCOUNT_SID')
authtoken=os.getenv('INPUT_TWILIO_AUTH')

if title is None:
    title = os.getenv('INPUT_PRTITLE')
if num is None:
    num = os.getenv('INPUT_PRNUM')
# ---------- Checking for responses ---------------

if event == "pull_request":
    github_url = f'https://github.com/{repo}/pulls/{num}'
    if action == "opened":
        response = f'A new Pull request *{title}* (*#{num}*) has been opened in *{repo}* by *{name}*  \n\n {github_url}'
        
    elif action == 'closed':
        response = f'The Pull request *{title}* (#{num}) on *{repo}* has been closed by *{name}*, \n\n {github_url}'
        elif event == 'issues':
    github_url = f'https://github.com/{repo}/issues/{num}'
    if action == 'opened':
        response = f'A new Issue *{title}* (*#{num}*) has been opened in *{repo}* by *{name}* \n\n {github_url}'
        
    elif action == 'closed':
        response = f'The Issue (*#{num}*) on *{repo}* was closed by *{name}*, \n\n {github_url}'

else:
    github_url = f'https://github.com/{repo}'
    response = f'A new *{event}* has been made in *{repo}* by *{name}*, \n\n {github_url}'


#creating twilio client

client=Client(account_sid,authtoken)
message = client.messages \
    .create(
         from_=From,
         body=response,
         to=To
     )
print('Message Sent')
