# English-Premier-league-sentiment-performance-correlation
Scrapes twitter using an API and analyzes sentiment. Each player's tweets are given a correlation score for their sentiment and their performance throughout the season based on Premier league statistics.

In order to gather player statistics, you'll need to download and set up the selenium web-driver. Make sure your path is edited in the stat-scraper.py script before running.

Both stat_scraper.py and twitter_api_scraper.py require sensitive information. stat_scraper will require your fantasy premier league information (username/password) and twitter_api_scraper will require your twitter API information. 

My players' tweets are stored in the 'Players' folder and their stats are stored in the text file 'stats.txt'.

Sentiment analysis and data visualization is completed by using the SentimentStatGrapher.ipynb jupyter notebook. 
My players' stats are stored in the last checkpoint.

-UTFT
