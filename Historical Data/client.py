# Create a Tweepy Client with the config parameters
# TO use Tweepy you have to install it by command "pip install tweepy"

import tweepy
import config

client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_secret,
    bearer_token=config.bearer_token
)