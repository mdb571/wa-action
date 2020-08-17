# Whatsapp Bot Github Action🚀
  This is a GitHub Action to notify the user about the changes in a github repo to Whatsapp via Bot. This will help the user track the overall workflow of the project directly form whatsapp

## Use
  Copy the [main.yml](https://github.com/mdb571/wa-action/blob/master/.github/workflows/main.yml) to your workflow<br>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; OR<br>
   Use the action directly form the actions marketplace [here]()
   
## Setup
1. Create a free twilio account [here](https://www.twilio.com/).  
2. From your twilio dashboard fetch ACCOUNT SID and AUTH TOKEN.
  <img alt="Twilio Dasboard" src="https://raw.githubusercontent.com/mdb571/covid-sms-notify/master/img/img2.png"/>
3. Join the twilio whatsapp sandbox by sending your join code to the twilio whatsapp number 
  <img alt="Twilio Sandbox" src="https://raw.githubusercontent.com/mdb571/wa-action/master/sandbox.jpeg"/>
  
4. Create the following secrets in your repository by going to settings>secrets

 SECRET          | Purpose                                              | 
------------------|-------------------------------------------------------|
FROM     | The twilio whatsapp bot number (default= ```+14155238886)```          | 
TO    | Your Whatsapp number                                              | 
TWILIO_ACCOUNT_SID        |twilio account sid obtained from your twilio dashboard|
TWILIO_AUTH  |twilio auth token obtained from your twilio dashboard  |  

## Screenshots
  <img alt="Sample" src="https://raw.githubusercontent.com/mdb571/wa-action/master/screen.jpeg"/>

## Support
 Give a :star2: if this project helped you!
