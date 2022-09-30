import tweepy

CONSUMER_KEY = "i7aR4bJ7g2j2FJ0NOTMm4EqIJ"
CONSUMER_SECRET = "UGLcpppqR77ZeyCkWeYzG88pDMpqXKhWjNmyPbRqijGKNXJUSn"
ACCESS_KEY = "1560747703776251904-OcK2EBhOICn4aWPaYbC5ha0R0ImtVw"
ACCESS_SECRET = "5WwZaECoGY0hTdR1xh58OaC8Fh0YwnvbGIiKvnzQTHAfs"

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
                       access_token_secret=ACCESS_SECRET)

client.create_tweet(text="le dernier single de Laylow, mozart pleurerait si il écoutait cela.")