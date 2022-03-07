import json
from collections import Counter
import os
import string
import nltk
import re
from nltk import bigrams 

#write_to_file function 
def write_to_file(data, filename):     
    filename= os.path.join(os.path.dirname(__file__), filename)
    with open(filename,"w") as mt:
	    json.dump(data, mt)
 
emoticons = r"""
    (?:
        [:=;] 
        [oO\-]? 
        [D\)\]\(\]/\\OpP]
    )"""
 
regex_strings = [
    emoticons,
    r'<[^>]+>', 
    r'(?:@[\w_]+)', 
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", 
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', 
    r"(?:[a-z][a-z'\-_]+[a-z])", 
    r'(?:[\w_]+)', 
    r'(?:\S)'
]
    
tokens_re = re.compile(r'('+'|'.join(regex_strings)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def process(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
filename= os.path.join(os.path.dirname(__file__), "data/search_stream_tweets.json")

punctuation = list(string.punctuation)
sw = nltk.corpus.stopwords.words('english') + punctuation + ['rt', 'via','RT','us','link','like','due']

with open(filename, 'r') as file:
    counter = Counter()
    for eachline in file:
        tweetsList = json.loads(eachline)
        for eachTweet in tweetsList:
            hashTags = [word for word in process(eachTweet['text']) if word.startswith('#')]
            counter.update(hashTags)

print("Most Common Hashtags")
# print(counter.most_common(15))
write_to_file(counter.most_common(15),'data/stream_hashtags.json')

with open(filename, 'r') as file:
    counter = Counter()
    for eachline in file:
        tweetsList = json.loads(eachline)
        for eachTweet in tweetsList:
            hashTags = [word for word in process(eachTweet['text']) if word.startswith('@')]
            counter.update(hashTags)

print("Most Common Mentions")
# print(counter.most_common(15))
write_to_file(counter.most_common(15),'data/stream_mention.json')


with open(filename, 'r') as file:
    counter = Counter()
    for eachline in file:
        tweetsList = json.loads(eachline)
        for eachTweet in tweetsList:
            occurring_word = [word for word in process(eachTweet['text']) if word not in sw and not word.startswith(('#', '@'))] 
            counter.update(occurring_word)

print("Most Occurring Words")
# print(counter.most_common(15))
write_to_file(counter.most_common(15),'data/stream_most_occurring_words.json')


with open(filename, 'r') as file:
    counter = Counter()
    for eachline in file:
        tweetsList = json.loads(eachline)
        for eachTweet in tweetsList:
            stopWords = [word for word in process(eachTweet['text']) if word not in sw]
            terms_bigram = bigrams(stopWords)
            counter.update(terms_bigram)

print("Bigrams")
# print(counter.most_common(15))
write_to_file(counter.most_common(15),'data/stream_bigrams.json')


