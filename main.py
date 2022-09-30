import json
import random
import time
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

tweetfilms = json.loads(open('tweetfilms.json', encoding='utf-8').read())
films = json.loads(open('films.json', encoding='utf-8').read())

tweetseries = json.loads(open('tweetseries.json', encoding='utf-8').read())
series = json.loads(open('series.json', encoding='utf-8').read())

tweetrappeurs = json.loads(open('tweetrappeurs.json', encoding='utf-8').read())
rappeurs = json.loads(open('rappeurs.json', encoding='utf-8').read())
albums = json.loads(open('albums.json', encoding='utf-8').read())
chansons = json.loads(open('chansons.json', encoding='utf-8').read())

tweetmangas = json.loads(open('tweetmangas.json', encoding='utf-8').read())
mangas = json.loads(open('mangas.json', encoding='utf-8').read())
persos = json.loads(open('perso.json', encoding='utf-8').read())

tweetdivers = json.loads(open('tweetdivers.json', encoding='utf-8').read())
streameurs = json.loads(open('streameurs.json', encoding='utf-8').read())
twittos = json.loads(open('twittos.json', encoding='utf-8').read())
youtubeurs = json.loads(open('youtubeurs.json', encoding='utf-8').read())
villes = json.loads(open('villes.json', encoding='utf-8').read())
listecategories = [1, 2, 3, 4]


def choose():
    count = 0
    #   choix = random.choices(listecategories,weights=(25,25,25,25),k=1)
    choix = random.randint(1,5)
    if choix == 5:
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
        film1 = random.choice(films)
        film2 = random.choice(films)
        film3 = random.choice(films)
        film4 = random.choice(films)

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
                                                  album1=album1,
                                                  album2=album2,
                                                  film1=film1,
                                                  film2=film2,
                                                  film3=film3,
                                                  film4=film4)
        twt = client.create_tweet(text=tweet)
        print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
        print(tweet)
    if choix == 4:
        manga1 = random.choice(mangas)
        manga2 = random.choice(mangas)
        manga3 = random.choice(mangas)
        manga4 = random.choice(mangas)
        perso1 = random.choice(persos)
        perso2 = random.choice(persos)
        perso3 = random.choice(persos)
        perso4 = random.choice(persos)
        mangatext = random.choice(tweetmangas)

        tweet = mangatext.format(manga1=manga1,
                                 manga2=manga2,
                                 manga3=manga3,
                                 manga4=manga4,
                                 perso1=perso1,
                                 perso2=perso2,
                                 perso3=perso3,
                                 perso4=perso4)
        bracketcountmanga = mangatext.count('{p')
        manga1 = manga1.lower() + '.png'
        manga2 = manga2.lower() + '.png'
        manga3 = manga3.lower() + '.png'
        manga4 = manga4.lower() + '.png'
        filenames = []
        rappeur = locals()
        if bracketcountmanga > 1:
            for i in range(bracketcountmanga):
                count += 1
                filenames.append(rappeur['manga' + str(count)])
        else:
            filenames = manga1
        media_ids = []
        if bracketcountmanga > 1:
            for i in filenames:
                res = API.media_upload(filename='temp', file=open('./perso/' + i, 'rb'))
                media_ids.append(res.media_id)
                time.sleep(1)
            twt = client.create_tweet(text=tweet, media_ids=media_ids)
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
        elif bracketcountmanga == 1:
            res = API.simple_upload(filename='temp', file=open('./rappeurs/' + filenames, 'rb'))
            twt = client.create_tweet(text=tweet, media_ids=[res.media_id])
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
            print(tweet)
        else:
            twt = client.create_tweet(text=tweet)
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
            print(tweet)
    elif choix == 3:
        tweet = random.choice(tweetfilms).format(random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(persos))
        twt = client.create_tweet(text=tweet)
        print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
        print(tweet)

    elif choix == 2:
        tweet = random.choice(tweetseries).format(random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series))
        try:
            twt = client.create_tweet(text=tweet)
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
            print(tweet)
        except Exception:
            print(Exception)
    elif choix == 1:
        rappeur1 = random.choice(rappeurs)
        rappeur2 = random.choice(rappeurs)
        rappeur3 = random.choice(rappeurs)
        rappeur4 = random.choice(rappeurs)
        twttext = random.choice(tweetrappeurs)

        tweet = twttext.format(r1=rappeur1,
                               r2=rappeur2,
                               r3=rappeur3,
                               r4=rappeur4,
                               a1=random.choice(albums),
                               a2=random.choice(albums),
                               a3=random.choice(albums),
                               a4=random.choice(albums),
                               a5=random.choice(albums),
                               a6=random.choice(albums),
                               c1=random.choice(chansons),
                               c2=random.choice(chansons),
                               c3=random.choice(chansons),
                               c4=random.choice(chansons),
                               c5=random.choice(chansons),
                               c6=random.choice(chansons))

        bracketcount = twttext.count('{r')
        rappeur1 = rappeur1.lower() + '.png'
        rappeur2 = rappeur2.lower() + '.png'
        rappeur3 = rappeur3.lower() + '.png'
        rappeur4 = rappeur4.lower() + '.png'
        filenames = []
        rappeur = locals()
        if bracketcount > 1:
            for i in range(bracketcount):
                count += 1
                filenames.append(rappeur['rappeur' + str(count)])
        else:
            filenames = rappeur1
        media_ids = []
        if bracketcount > 1:
            for i in filenames:
                res = API.media_upload(filename='temp', file=open('./rappeurs/' + i, 'rb'))
                media_ids.append(res.media_id)
                time.sleep(1)
            twt = client.create_tweet(text=tweet, media_ids=media_ids)
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
            print(tweet)
        else:
            res = API.simple_upload(filename='temp', file=open('./rappeurs/' + filenames, 'rb'))
            twt = client.create_tweet(text=tweet, media_ids=[res.media_id])
            print('https://twitter.com/Shironeutron/status/' + twt.data['id'])
            print(tweet)
    else:
        pass


if __name__ == '__main__':
    while 1:
        try:
            choose()
            time.sleep(random.randint(5400, 10080))
        except:
            pass
