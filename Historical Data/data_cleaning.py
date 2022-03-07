import string
import pandas as pd
import html
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import nltk

pd.set_option('display.max_colwidth', None)
#read our search_recent_tweets json file (from search_tweet.py)
filename= os.path.join(os.path.dirname(__file__), "data/search_recent_tweets.json")
data = pd.read_json(filename)
data.head()

#Task 1: Remove duplicates and save to new file
print("####Removing Duplicates####")

data_n = data.drop_duplicates(subset=['id','text'],keep='first') 
data_n.head()
no_duplicates_file= os.path.join(os.path.dirname(__file__), "data/no_duplicates.json")
data_n.to_json(no_duplicates_file)

print("####Removed Duplicates####")
print("##########################")

#let's extract tweets
new_data = pd.read_json(no_duplicates_file)
new_data.head()
tweets = new_data['text']
tweets.head()

#Task 2: Cleaning html and save to a new file
print("####Removing HTML####")
tweets_to_remove_html = tweets
for i in range (len(tweets_to_remove_html)):
    x = tweets_to_remove_html[i].replace('\n','') 
    tweets_to_remove_html[i] = html.unescape(x)
    tweets_to_remove_html.head()

no_html_file= os.path.join(os.path.dirname(__file__), "data/no_html.json")
tweets_to_remove_html.to_json(no_html_file)

print("####Removed HTML####")
print("##########################")

#Task 3: Clean up words with Hash #
print("####Removing HASH####")
tweets_to_remove_hash = tweets
for i in range (len(tweets_to_remove_hash)):
    tweets_to_remove_hash[i] = re.sub(r'(@[A-Za-z0–9_]+)|[^\w\s]|#|http\S+', '', tweets_to_remove_hash[i])
    tweets_to_remove_hash.head()

no_hash_file= os.path.join(os.path.dirname(__file__), "data/no_hash.json")
tweets_to_remove_hash.to_json(no_hash_file)
print("####Removed HASH####")
print("##########################")

#Task 4: Tokenize
print("####About to tokenize")
print("##########################")
tweets_to_token = tweets

for i in range(len(tweets_to_token)):
    tweets_to_token[i] = word_tokenize(tweets_to_token[i])

tokenized_file= os.path.join(os.path.dirname(__file__), "data/no_tokenize.json")
tweets_to_token.to_json(tokenized_file)

print("####Tokenized###")
print("##########################")

#Task 5: Remove stopwords
print("####About to remove stopwords####")
print("##########################")

tweets_stopwords = tweets
punctuation = list(string.punctuation)
sw = nltk.corpus.stopwords.words('english') + punctuation + ['rt', 'via', 'RT']

for i in range(len(tweets_stopwords)):
    tweets_stopwords[i] = [word for word in tweets_stopwords[i] if not word in sw]

no_stopwords_file= os.path.join(os.path.dirname(__file__), "data/no_stopwords.json")
tweets_stopwords.to_json(no_stopwords_file)

print("####Removed stopwords###")
print("##########################")