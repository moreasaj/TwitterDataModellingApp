# Search for recents tweets using a keyword and write output to json file

from re import I
from client import streaming_client;
import json;
import os
import config
import tweepy

#write_to_file function 
def write_to_file(tweet):     
    filename= os.path.join(os.path.dirname(__file__), "data/search_stream_tweets.json")
    with open(filename,"w") as mt:
        json.dump(tweet, mt)
    print("done")
    
jsonData = []
i = 1

class clsStreaming(tweepy.StreamingClient):
       
    def on_tweet(self, tweet):
        global i
        jsonData.append(tweet.data)
        i=i + 1
        print(i)

        if (i==10500):
            write_to_file(jsonData)

printer = clsStreaming(config.bearer_token,wait_on_rate_limit=True)
# printer.add_rules(tweepy.StreamRule("accounting","accounting"))
printer.filter()

