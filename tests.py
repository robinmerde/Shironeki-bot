import json
import tweepy
import time

CREDENTIALS = json.loads(open('credentials.json', encoding='utf-8').read())

CONSUMER_KEY = CREDENTIALS['key']
CONSUMER_SECRET = CREDENTIALS['key_secret']
ACCESS_KEY = CREDENTIALS['token']
ACCESS_SECRET = CREDENTIALS['token_secret']

auth = tweepy.OAuthHandler(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_KEY,
    access_token_secret=ACCESS_SECRET
)
API = tweepy.API(auth)

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_KEY,
                       access_token_secret=ACCESS_SECRET
                       )

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('Streaming API connectée')

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            client.like(tweet)

        time.sleep(0.1)

stream = MyStream(bearer_token=CREDENTIALS['bearer'])
stream.add_rules(tweepy.StreamRule('ta gueule'))

stream.filter(tweet_fields=["referenced_tweets"])