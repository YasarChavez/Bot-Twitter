import time
import credentials
import tweepy
import random
from tweepy import OAuthHandler
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

#retweet a tweet based on a term
def retweet():
    print("Ingrese termino de busqueda para dar RT 🔍:")
    termino = input()
    print("Ingrese cantidad de tweets a dar RT:")
    cantidad = input()
    cantidad = int(cantidad)
    print("Ingrese tiempo entre RT (en segundos) ⏰:")
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
            tweet.retweet()
            print("RT ✅")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
            time.sleep(tiempo)
        return