import json
import random
import time

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
    choix = 1
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
        nbr1 = str(random.randint(1,25))
        nbr2 = str(random.randint(1,25))

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
                                                  nbr1 = nbr1,
                                                  nbr2 = nbr2)
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
        print(tweet)
    elif choix == 3:
        tweet = random.choice(tweetfilms).format(random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(films),
                                                 random.choice(persos))
        print(tweet)

    elif choix == 2:
        tweet = random.choice(tweetseries).format(random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series),
                                                  random.choice(series))
        try:
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

        print(tweet)
    else:
        pass


if __name__ == '__main__':
    while 1:
        try:
            choose()
            time.sleep(1)
        except:
            pass