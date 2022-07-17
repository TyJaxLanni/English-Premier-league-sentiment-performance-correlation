#!/usr/bin/env python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import time

def getSentiment(playerName):

	sid_obj = SentimentIntensityAnalyzer()
	
	neutral_count = 0
	positive_count = 0
	negative_count = 0

	with open(playerName + ".txt", 'r') as f:
		for tweet in f:
			sentiment_dict = sid_obj.polarity_scores(tweet)
	
	
			# decide sentiment as positive, negative and neutral
			if sentiment_dict['compound'] >= 0.05 :
				positive_count += 1
		
			elif sentiment_dict['compound'] <= - 0.05 :
				negative_count += 1
		
			else:
				neutral_count += 1
	
		print("neutral: " + str(neutral_count))
		print("positive: " + str(positive_count))
		print("negative: " + str(negative_count))
	
		sentDict = dict()
		sentDict['neutral'] = neutral_count
		sentDict['positive'] = positive_count
		sentDict['negative'] = negative_count
	
		return sentDict	



def findTweets(playerName):

	print("donig stuff")

	#SAVE YOUR API KEYS HERE

	API_KEY = 'YOUR API KEY HERE'
	API_SECRET_KEY = 'YOUR SECRET KEY HERE'
	ACCESS_TOKEN = 'YOUR ACCESS TOKEN HERE'
	ACCESS_SECRET_TOKEN = 'YOUR SECRET TOKEN HERE'
	
	auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
	api = tweepy.API(auth)
	
	search_words = playerName + " Everton" + " -filter:retweets"
	#August 1st
	date_since = "2020-01-08"

	time.sleep(2)
	tweets = tweepy.Cursor(api.search, q = search_words, lang='en', since=date_since, tweet_mode='extended').items(10000)
	texts = [tweet.full_text for tweet in tweets]
	

	with open(playerName.replace(' ', '') + ".txt", "w") as f:
		for line in texts:
			print(line, file=f)



def main():
	print("hello")
	teamDict = dict()

	with open("stats.txt", 'r', encoding="ISO-8859-1") as f:
		for line in f:
			pairs = line.split(',')
			playerDict = dict()
			for i in pairs:
				i = i.replace("'", "").replace("{", "").replace("}", "").strip()
				li = i.split(":")
				for j in range(len(li)):
					li[j] = li[j].replace(' ', '')
				print(i)
				playerDict[li[0]] = int(li[1]) if li[1].isnumeric() else li[1]

			teamDict[playerDict['name']] = playerDict

	nameList = [player for player in teamDict.keys()]
	#for player in nameList[0:12]:
	#	print(player.replace('-', ' '))
	#	findTweets(player.replace('-', ' '))

	#need to split into two groups because of twitter request limits
	#for player in nameList[12:]:
	#	print(player.replace('-', ' '))
	#	findTweets(player.replace('-', ' '))

	for player in teamDict.keys():
		print(player.replace('-', ' '))
		teamDict[player]["sentiment"] = getSentiment(player.replace('-', ''))
		print(teamDict[player]["sentiment"])






if __name__ == "__main__":	
	main()
