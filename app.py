import os


title = os.getenv("INPUT_IUTITLE")
num = os.getenv("INPUT_IUNUM")
name = os.getenv('GITHUB_ACTOR')
event = os.getenv("GITHUB_EVENT_NAME")
repo = os.getenv("GITHUB_REPOSITORY")
action = os.getenv('INPUT_EVENT_ACTION')
From = os.getenv('INPUT_FROM')
To = os.getenv('INPUT_TO')
apikey=os.getenv('INPUT_TWILIO_API')
authtoke=os.getenv('INPUT_TWILIO_AUTH')

twilio_url='https://api.twilio.com/2010-04-01/Accounts/'+apikey+'/Messages.json'


if title is None:
    title = os.getenv('INPUT_PRTITLE')
if num is None:
    num = os.getenv('INPUT_PRNUM')
# ---------- Checking for responses ---------------

if event == "pull_request":
    github_url = f'https://github.com/{repo}/pulls/{num}'
    if action == "opened":
        response = f'A new Pull Request (#{num}) is opened in {repo} by {name} with title: \"{title}\" URL: {github_url}'
        data={
         'To':To,
         'From':From,
         'Body':response
        }
        request.post(twilio_url,data=data,auth=(apikey,authtoken))
    elif action == 'closed':
        response = f'The Pull Request (#{num}) on {repo} is closed by {name}, URL: {github_url}'
        data={
         'To':To,
         'From':From,
         'Body':response
        }
        request.post(twilio_url,data=data,auth=(apikey,authtoken))
elif event == 'issues':
    github_url = f'https://github.com/{repo}/issues/{num}'
    if action == 'opened':
        response = f'A new Issue (#{num}) is opened in {repo} by {name} with title: \"{title}\" URL: {github_url}'
        data={
         'To':To,
         'From':From,
         'Body':response
        }
        request.post(twilio_url,data=data,auth=(apikey,authtoken))
    elif action == 'closed':
        response = f'The Issue (#{num}) on {repo} is closed by {name}, URL: {github_url}'
        data={
         'To':To,
         'From':From,
         'Body':response
        }
        request.post(twilio_url,data=data,auth=(apikey,authtoken))

else:
    github_url = f'https://github.com/{repo}'
    response = f'A new {event} has occured in the {repo} by {name},URL: {github_url}'
    data={
         'To':To,
         'From':From,
         'Body':response
        }
    request.post(twilio_url,data=data,auth=(apikey,authtoken))
