import time
import credentials
import tweepy
import random
from tweepy import OAuthHandler
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


#Like tweets
def likeTweets():
    print("Ingrese termino de busqueda para dar Like 🔍:")
    termino = input()
    print("Ingrese cantidad de tweets a dar Like:")
    cantidad = input()
    cantidad = int(cantidad)
    print("Ingrese tiempo entre Like(en segundos) ⏰:")
    tiempo = input()
    tiempo = int(tiempo)
    print("Presione Ctrl+C para detener")
    for tweet in tweepy.Cursor(api.search, q=termino, lang="es").items(cantidad):
        try:
            tweet.favorite()
            print("Like 💙")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        time.sleep(tiempo)
    return
#Like tweets random time
def likeTweetsRandom():
    print("Ingrese termino de busqueda para dar Like 🔍:")
    termino = input()
    print("Ingrese cantidad de tweets a dar Like:")
    cantidad = input()
    cantidad = int(cantidad)
    print("Ingrese tiempo entre Like(en segundos) ⏰:")
    print("Ingrese tiempo minimo:")
    tmin = input()
    tmin = int(tmin)
    print("Ingrese tiempo maximo:")
    tmax = input()
    tmax = int(tmax)
    tiempo = random.randint(tmin,tmax)
    print("Presione Ctrl+C para detener")
    for tweet in tweepy.Cursor(api.search, q=termino, lang="es").items(cantidad):
        try:
            tweet.favorite()
            print("Like 💙")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        time.sleep(tiempo)
    return

def likeHome():
    print("Ingrese cantidad de tweets a dar Like:")
    cantidad = input()
    cantidad = int(cantidad)
    print("Ingrese tiempo entre Like(en segundos) ⏰:")
    print("Ingrese tiempo minimo:")
    tmin = input()
    tmin = int(tmin)
    print("Ingrese tiempo maximo:")
    tmax = input()
    tmax = int(tmax)
    tiempo = random.randint(tmin,tmax)
    print("Presione Ctrl+C para detener")
    for tweet in tweepy.Cursor(api.home_timeline).items(cantidad):
        try:
            tweet.favorite()
            print("Like 💙")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
        time.sleep(tiempo)
    return