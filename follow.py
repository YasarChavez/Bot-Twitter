import time
import credentials
import tweepy
import random
from tweepy import OAuthHandler
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)


def follow_random_users():
    #Get users by term
    palabra = input("Introduce una palabra para buscar 🔍: ")
    print("Comenzando a seguir usuarios aleatorios")
    print("Presione Ctrl+C para detener")
    print(" ")
    while True:
        try:
            users = api.search_users(q = palabra, count = 100)
            #Choose a random user
            user = random.choice(users)
            #Follow the user
            api.create_friendship(user.id)
            print("✅ Usuario seguido con id: " + str(user.id) + " y de nombre: " + user.name)
            #Wait for a random amount of time
            time.sleep(random.randint(10,60))
            continue
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(60)
            continue
        except StopIteration:
            break
        except KeyboardInterrupt:
            break
        except:
            print("Error inesperado ❌")
            time.sleep(60)
            continue
        finally:
            print("Reiniciando 🔄")
            time.sleep(60)
            continue
