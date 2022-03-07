# Search for recents tweets using a keyword and write output to json file

from distutils.command.config import config
from client import client;
import json;
import os
import config

searchWord=config.search_keyword
fields=config.search_fields

#write_to_file function 
def write_to_file(tweet):     
    filename= os.path.join(os.path.dirname(__file__), "data/search_recent_tweets.json")
    with open(filename,"w") as mt:
	    json.dump(tweet, mt)

#search recent tweets
searchResults = client.search_recent_tweets(query=searchWord, max_results=100).data #, tweet_fields=[fields])

jsonData = []  #json array
for tweet in searchResults: #iterate through the searchResults and add to the json array
    jsonData.append(tweet.data) 

#output our json data to file
write_to_file(jsonData)

print("done")


