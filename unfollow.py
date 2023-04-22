import time
import credentials
import tweepy
import random
from tweepy import OAuthHandler
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

def unfollow():
    for follower in tweepy.Cursor(api.followers).items(100):
        follower.unfollow()
        user = api.me()
        print("Unfollow : " + follower.screen_name + "✅")
        time.sleep(2)
        print("Cantidad de follows actual: " + str(user.friends_count))
        print("Esperando... ⏱︰")
        time.sleep(random.randint(60,300))
    print("Unfollow completo ✅")