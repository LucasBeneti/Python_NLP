import tweepy
from textblob import TextBlob

consumer_key = 'NN6yIQnqhkRkPaLLOc6nxz9SL'
consumer_secret = 'HG2dyZo9kmKhGP2IyO1DoRNt61sbWyXkL88PFim2xAm9HrzaDp'

access_token = '52823941-puZpC5DsWqXP0TBtMKktht1KXCIiZHm2yLVIJMMBI'
access_token_secret = 'ptY96nwRrUAZ0JcC3ZIRBkqBOsxycLXQzy66HkPHXV3BF'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('bitcoin')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)