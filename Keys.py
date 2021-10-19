consumer_key = 'nRHnWxfh3mhobVJmRETAsV3Dp'
consumer_secret = 'vcp8ub2jIazOBFcuH5BniuIqhJUXTsHmVASRZ28qo6FFxb31Xi'
access_token = '97425271-KLBCYf3mgHwSx6D7agME84nOZr2DkybfbLe2H6Dvg'
access_token_secret = 'oNLEfxR9Ogncnd2eASgWL4K4TslnsvwmAhIpxW3FRRvja'
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_term = ('$MU')

cursor = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(10)

for i in cursor:
    clean_tweet = i.text.replace('RT', ' ')
    if clean_tweet.startswith(' @'):
        position = clean_tweet.index(':')
        clean_tweet = clean_tweet[position+2:]
    if clean_tweet.startswith('@'):
        position = clean_tweet.index(' ')
        clean_tweet = clean_tweet[position+2:]
    print(clean_tweet)

