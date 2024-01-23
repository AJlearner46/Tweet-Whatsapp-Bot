
import tweepy
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import requests

access_token = 'acess_token'
access_token_secret = 'acess_token_secret'
api_key = 'api_key'
api_key_secret = 'api_key_secret'
# client_id = ''
# client_secret = ''
# bearer_token = ''

# From Twilio
account_sid = 'account_sid'
auth_token = 'auth_token'
twilio_phone_number = 'your_twilio_number'



# Flask app 
app = Flask(__name__)


#auth = tweepy.OAuthHandler(api_key, api_key_secret)
#auth.set_access_token(access_token, access_token_secret)

#auth.access_token = bearer_token
#twitter_api = tweepy.API(auth )

client = tweepy.Client(consumer_key=api_key,
                    consumer_secret=api_key_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)


@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    incoming_message = request.values.get('Body', '').lower()

    if incoming_message.startswith('tweet:'):
        tweet_text = incoming_message[6:].strip()
        post_tweet(tweet_text)
        response_message = "Tweet posted successfully!"
    else:
        response_message = "Invalid command. To tweet, use 'Tweet: your tweet content.'"

    twilio_response = MessagingResponse()
    twilio_response.message(response_message)

    return str(twilio_response)

def post_tweet(tweet_text):
    #twitter_api.update_status(status=tweet_text)
    client.create_tweet(text=tweet_text)
    
if __name__ == '__main__':
    app.run(port=5000)