import tweepy
#Import csv
import csv
from textblob import TextBlob

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information 
# on Twitter's OAuth implementation.

consumer_key = 'XXX'
consumer_secret = 'XXX'

access_token = 'XXX'
access_token_secret = 'XXX'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
# Open/create a file to append data to
csvFile = open('result.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

#wordToSearch
wordToSearch = "Lionel Messi"
public_tweets = api.search(wordToSearch)

# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)

for tweetSecond in tweepy.Cursor(api.search,
                           q = wordToSearch,
                           since = "2018-03-13",
                           until = "2018-03-14",
                           lang = "en").items():
    
    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweetSecond.created_at, tweetSecond.text.encode('utf-8')])
    print (tweetSecond.created_at, tweetSecond.text)
csvFile.close()