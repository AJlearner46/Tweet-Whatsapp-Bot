# TweetWhatsapp-Bot

## Simple Python Bot with the help of that we can Tweet from whatsapp 

  - #### Whatsapp
       - ![WhatsApp Image 2024-01-24 at 00 07 59_33493294](https://github.com/AJlearner46/TweetWhatsapp-Bot/assets/99804336/6cfba525-8f0d-42af-b371-1c0df90a2fd5)




  - #### Twitter(X)
       - ![WhatsApp Image 2024-01-24 at 00 08 29_f3521dbf](https://github.com/AJlearner46/TweetWhatsapp-Bot/assets/99804336/7d0c54ac-375e-4f44-b580-ac524036e04c)
   

# Step For Locally Run 
#### - 1. Create Twilio Account then obtain account_sid, auth_token and your twilio number
#### - 2. From Twitter developer account create new App, give read & write permission then obtain access_token, access_token_secret, api_key, api_key_secret.
#### - 3. Run TweetFromWP.py file local 
#### - 4. then you have to use ngrok for obtain Ngrok public url
#### - 5. now from Twilio Console, navigate to your WhatsApp Sandbox configuration, and update the Inbound Webhook URL to the Ngrok public URL (https://your-ngrok-subdomain.ngrok.io/whatsapp) and select POST
#### - 6. Now you're ready to test bot : send a WhatsApp message to your Twilio number, and it should be handled by your Flask application running locally through Ngrok.



