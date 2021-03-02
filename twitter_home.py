import tweepy
import math
import numpy as np
import bilgiler

consumer_key = bilgiler.consumer_key
consumer_secret = bilgiler.consumer_secret
access_token = bilgiler.access_token
access_token_secret = bilgiler.access_token_secret


auth = tweepy.OAuthHandler (consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
liste = []
for tweet in public_tweets:
    liste.append(tweet.text)
    print(tweet.text)
    print("\n")
    


