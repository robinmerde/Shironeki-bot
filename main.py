import json
import random
import time
import tweepy
import os

# Importer les tokens de l'API

CREDENTIALS = json.loads(open('Q:\home\pi\Documents\Shironeutron-credentials\credentials.json', encoding='utf-8').read())

CONSUMER_KEY = CREDENTIALS['key']
CONSUMER_SECRET = CREDENTIALS['secret_key']
ACCESS_KEY = CREDENTIALS['token']
ACCESS_SECRET = CREDENTIALS['secret_token']

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

# Je charge tous les json sur le programme


# OBJETS

films = json.loads(open('films.json', encoding='utf-8').read())
series = json.loads(open('series.json', encoding='utf-8').read())
rappeurs = json.loads(open('rappeurs.json', encoding='utf-8').read())
albums = json.loads(open('albums.json', encoding='utf-8').read())
chansons = json.loads(open('chansons.json', encoding='utf-8').read())
mangas = json.loads(open('mangas.json', encoding='utf-8').read())
persosmangas = json.loads(open('persosmangas.json', encoding='utf-8').read())
streameurs = json.loads(open('streameurs.json', encoding='utf-8').read())
twittos = json.loads(open('twittos.json', encoding='utf-8').read())
youtubeurs = json.loads(open('youtubeurs.json', encoding='utf-8').read())
villes = json.loads(open('villes.json', encoding='utf-8').read())

screens_chansons = os.listdir("./screens-chansons/")
# FORMATS

tweetdivers = json.loads(open('tweetdivers.json', encoding='utf-8').read())


odds = ['tweet', 'screen']


def choose():
    choix = random.choices(odds, weights=(100,10))
    print(choix[0])

    if choix[0] == 'tweet':
        #   Randomisation des objets

        yt1 = random.choice(youtubeurs)
        yt2 = random.choice(youtubeurs)
        yt3 = random.choice(youtubeurs)
        yt4 = random.choice(youtubeurs)
        ville1 = random.choice(villes)
        ville2 = random.choice(villes)
        ville3 = random.choice(villes)
        ville4 = random.choice(villes)
        rappeur1 = random.choice(rappeurs)
        rappeur2 = random.choice(rappeurs)
        rappeur3 = random.choice(rappeurs)
        rappeur4 = random.choice(rappeurs)
        twittos1 = random.choice(twittos)
        twittos2 = random.choice(twittos)
        twittos3 = random.choice(twittos)
        twittos4 = random.choice(twittos)
        streamer1 = random.choice(streameurs)
        streamer2 = random.choice(streameurs)
        streamer3 = random.choice(streameurs)
        streamer4 = random.choice(streameurs)
        musique1 = random.choice(chansons)
        musique2 = random.choice(chansons)
        musique3 = random.choice(chansons)
        musique4 = random.choice(chansons)
        album1 = random.choice(albums)
        album2 = random.choice(albums)
        album3 = random.choice(albums)
        album4 = random.choice(albums)
        film1 = random.choice(films)
        film2 = random.choice(films)
        film3 = random.choice(films)
        film4 = random.choice(films)
        serie1 = random.choice(series)
        serie2 = random.choice(series)
        serie3 = random.choice(series)
        serie4 = random.choice(series)
        manga1 = random.choice(mangas)
        manga2 = random.choice(mangas)
        manga3 = random.choice(mangas)
        manga4 = random.choice(mangas)
        persomanga1 = random.choice(persosmangas)
        persomanga2 = random.choice(persosmangas)
        persomanga3 = random.choice(persosmangas)
        persomanga4 = random.choice(persosmangas)


        # Creation du tweet

        tweet = random.choice(tweetdivers).format(yt1 = yt1,
    yt2 = yt2,
    yt3 = yt3,
    yt4 = yt4,
    ville1 = ville1,
    ville2 = ville2,
    ville3 = ville3,
    ville4 = ville4,
    rappeur1 = rappeur1,
    rappeur2 = rappeur2,
    rappeur3 = rappeur3,
    rappeur4 = rappeur4,
    twittos1 = twittos1,
    twittos2 = twittos2,
    twittos3 = twittos3,
    twittos4 = twittos4,
    streamer1 = streamer1,
    streamer2 = streamer2,
    streamer3 = streamer3,
    streamer4 = streamer4,
    musique1 = musique1,
    musique2 = musique2,
    musique3 = musique3,
    musique4 = musique4,
    album1 = album1,
    album2 = album2,
    album3 = album3,
    album4 = album4,
    film1 = film1,
    film2 = film2,
    film3 = film3,
    film4 = film4,
    serie1 = serie1,
    serie2 = serie2,
    serie3 = serie3,
    serie4 = serie4,
    manga1 = manga1,
    manga2 = manga2,
    manga3 = manga3,
    manga4 = manga4,
    persomanga1 = persomanga1,
    persomanga2 = persomanga2,
    persomanga3 = persomanga3,
    persomanga4 = persomanga4)

        # Tweets avec images (rappeurs)

        rappeur1 = rappeur1.lower() + '.png'
        rappeur2 = rappeur2.lower() + '.png'
        rappeur3 = rappeur3.lower() + '.png'
        rappeur4 = rappeur4.lower() + '.png'
        filenames = []
        local = locals()

        # Mettre le nom de chaque rappeur dans la liste filenames

        if tweet.count('rappeur4') >= 1:
            for i in range(1,5):
                filenames.append(local['rappeur' + str(i)])

        elif tweet.count('rappeur3') >= 1:
            for i in range(1,4):
                filenames.append(local['rappeur' + str(i)])

        elif tweet.count('rappeur2') >= 1:
            for i in range(1,3):
                filenames.append(local['rappeur' + str(i)])

        elif tweet.count('rappeur1') >= 1:
            filenames = rappeur1
        else:
            pass

        media_ids = []

        if tweet.count('rappeur1') >= 1:
            if tweet.count('rappeur2') >= 1:

                # Upload sur le "Media Studio" chaque nom et met leur "media id" dans la liste media_ids

                for i in filenames:
                    res = API.media_upload(filename='temp', file=open('./rappeurs/' + i, 'rb'))
                    media_ids.append(res.media_id)
                    time.sleep(1)

            else:
                res = API.simple_upload(filename='temp', file=open('./rappeurs/' + filenames, 'rb'))

            twt = client.create_tweet(text=tweet, media_ids=media_ids)
        else:
            twt = client.create_tweet(text=tweet)
        print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
        print(tweet)

    elif choix == "screen":
        screen = API.simple_upload(filename='temp', file='./screens-chansons/' + random.choice(screens_chansons))
        client.create_tweet(media_ids=screen.media_ids)


if __name__ == '__main__':

    while 1:
        choose()
        time.sleep(random.randint(5400, 10080))
