import tweepy
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)


question = raw_input('Are we updating with a picture or text?')

if(question == 'picture'):
    photo_path = 'C:\Users\gabri\Desktop\wallpapers\87.jpg'
    tweet = 'tweeting picture from bot'
    api.update_with_media(photo_path, tweet)
    print("picture tweeted!")
elif(question == 'text'):
    tweet = raw_input('What would you like to tweet?\n')
    api.update_status(tweet)
    print('tweet sent!')






