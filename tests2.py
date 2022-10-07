import tweepy
import json

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

tweet = 'papaapa~ la coupe'.partition('~')[0]
print(tweet, type(tweet))