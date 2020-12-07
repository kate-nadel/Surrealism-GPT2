import tweepy #via pip
import json #local
import random #built in

def lambda_handler(event, context):

# the finalize JSON file of generated text you want posted to bot
    tweet_data = json.load(open("Surrealist_tweets_compiled.json"))

    random_tweet = random.choice(tweet_data)

    consumer_key = "your key here"
    consumer_secret = "your key here"
    access_token = "your key here"
    access_token_secret = "your key here"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    api = tweepy.API(auth)

    tweet_post_result = api.update_status(random_tweet)

    return{
        "statusCode":200,
        "body":json.dumps("It worked!")
    }
