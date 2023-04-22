import time
import credentials
import tweepy
import random
import requests
import shutil
from tweepy import OAuthHandler
import os
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)

def imageTweet():
    #carpeta con imagenes
    carpeta = 'images/'
    #lista de imagenes
    imagenes = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
    #seleccionar una imagen aleatoria
    imagen = random.choice(imagenes)
    #ruta de la imagen
    ruta = carpeta + imagen
    #tweet con la imagen
    print("Enviando tweet con imagen... ⏰")
    time.sleep(3)
    api.update_with_media(ruta)
    print("Tweet con imagen enviado con éxito ✅")
    time.sleep(3)
    #borrar imagen?
    print("Borrar imagen? (s/n)")
    rta = input()
    if rta == "s":
        print("Borrando imagen... ⏳")
        time.sleep(3)
        os.remove(ruta)
        print("Imagen borrada 🚮")
        time.sleep(3)
        return
    else:
        print("Imagen no borrada 😁")
        return
    