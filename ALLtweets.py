import os
import tweepy as tw
import pandas as pd

# API keys
consumer_key= 'xJOSOBQIFQQZOKMAzZGf8RJvP'
consumer_secret= 'lkGh7uy3XeGKwuGWeXfjg5ud1wEb8VYFzcZTjjvH0XmNKsTNri'
access_token= '1420131687107813380-EUigVAo0abFTQUl62g0SZBeZAi7rFL'
access_token_secret= 'gQjlYJh2eDPN4kN5nnw59MP3axldx6P7wZ6YDhkFwwkbJ'

# Tweepy Authentication
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the variables of the search (player name, amount of tweets to be fetched, and start date of the search)
firstName = 'Patrick'
lastName = 'Mahomes'
fullname = firstName + lastName
search_words = "{}+{} OR {} -filter:retweets".format(firstName, lastName, lastName)

date_since = "2021-11-13"
numTweets = 5

# API fetch request
tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en",
              since=date_since).items(numTweets)


# Collect tweets in list
tweetData = [[tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8'), tweet.user.location.encode('utf-8')] for tweet in tweets]

# Create pandas dataframe
# tweet_text = pd.DataFrame(data=tweetData, 
#                     columns=['user', 'content', 'location'])

# tweet_text.to_csv('test.csv') 

# Print tweets
for tweet in tweetData:
     print(tweet)

