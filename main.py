import json
import random
import time
import tweepy


# Importer les tokens de l'API

CREDENTIALS = json.loads(open('credentials.json',encoding='utf-8').read())

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


aliases_format = json.loads(open('aliases-format.json',encoding="utf-8").read())

listecategories = [1,2]


def choose():

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

    # FORMATS

    tweetdivers = json.loads(open('tweetdivers.json', encoding='utf-8').read())

    count = 0

    choix = random.choices(listecategories,weights=(90,10),k=1)

    if choix == 1:
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

        tweet = random.choice(tweetdivers).format(**aliases_format)

        # Tweets avec images (rappeurs)

        
        rappeur1 = rappeur1.lower() + '.png'
        rappeur2 = rappeur2.lower() + '.png'
        rappeur3 = rappeur3.lower() + '.png'
        rappeur4 = rappeur4.lower() + '.png'
        filenames = []
        rappeurs = locals()

        # Mettre le nom de chaque rappeur dans la liste filenames

        if tweet.count('rappeur4') >= 1:
            for i in range(4):
                filenames.append(rappeurs['rappeur' + str(i)])

        elif tweet.count('rappeur3') >= 1:
            for i in range(3):
                filenames.append(rappeurs['rappeur' + str(i)])

        elif tweet.count('rappeur2') >= 1:
            for i in range(2):
                filenames.append(rappeurs['rappeur' + str(i)])

        elif tweet.count('rappeur1') >= 1:
            filenames = rappeur1
        else:
            pass


        media_ids = []

        if tweet.count('rappeur1') >= 1:
            if tweet.count('rappeur2') >= 1:

                    # Upload sur le "Media Studio" chaque nom et met leur "media id" dans la liste media_ids

                for i in filenames:
                    res = API.media_upload(filename='temp',file=open('./rappeurs/' + i, 'rb'))
                    media_ids.append(res.media_id)
                    time.sleep(1)

            else:
                res = API.simple_upload(filename='temp',file=open('./rappeurs/' + filenames, 'rb'))

            twt = client.create_tweet(text=tweet, media_ids=media_ids)
        else:
            twt = client.create_tweet(text=tweet)
        print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
        print(tweet)


if __name__ == '__main__':
    while 1:
        
        choose()
        time.sleep(random.randint(5400, 10080))
