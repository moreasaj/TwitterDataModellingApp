# Create a Tweepy Client with the config parameters
# TO use Tweepy you have to install it by command "pip install tweepy"

import tweepy
import config

streaming_client = tweepy.StreamingClient(config.bearer_token)
