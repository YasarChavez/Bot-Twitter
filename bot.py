import credentials
import tweepy

# Autenticación
from tweepy import OAuthHandler
auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
auth.set_access_token(credentials.access_token, credentials.access_token_secret)
api = tweepy.API(auth)



# Obtener información del usuario
user = api.verify_credentials()

# Get my user
print("")
print("Bienvenido " + user.screen_name +"!")
print("Cantidad de Followers: " + str(user.followers_count))
print("Cantidad de Following: " + str(user.friends_count))
print("")
#Menu
print("Menu:")
print("1. Nuevo Tweet 🐦(Ingresar texto)")
print("2. Like Tweets 💙(Tiempo Fijo)")
print("3. Like Tweets 💙(Tiempo Random)")
print("4. Like Tweets💙(HomePage)")
print("5. Dar RT 🔁(Tiempo Random)")
print("6. Seguir Usuarios aleatorios 🚻(Tiempo Random)")
print("7. Tweet con imagen aleatoria 📷(Carpeta 'images')")
print("8. Unfollow 💔(100 Personas - Tiempo Random entre 1 y 5 minutos)")

print(" ")
opcion = input("Ingrese una opción: ")

if opcion == "1":
    print("Nuevo tweet 🐦")
    tweet = input("Ingrese un tweet 📃: ")
    api.update_status(tweet)
    print("Tweet enviado ✅")
    print("")
elif opcion == "2":
    from likeTweets import likeTweets
    likeTweets()
    print("")
elif opcion == "3":
    from likeTweets import likeTweetsRandom
    likeTweetsRandom()
    print("")
elif opcion == "4":
    from likeTweets import likeHome
    likeHome()
    print("")
    
elif opcion == "5":
    from retweet import retweet
    retweet()
    print("")
    
elif opcion == "6":
    from follow import follow_random_users
    follow_random_users()
    print("")
elif opcion == "7":
    from imageTweet import imageTweet
    imageTweet()
    print("")
elif opcion == "8":
    from unfollow import unfollow
    unfollow()
    print("")
else:
    print("Opción incorrecta!")
    print("")
