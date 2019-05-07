import pandas as pd
import os.path
import json
from glob import glob
from time import strptime
from datetime import datetime
from dateutil import relativedelta

############################################################
# Utility Function
def tweet_age(user_time, tweet_time):
	user_day = user_time.split()[2]
	user_month = strptime(user_time.split()[1],'%b').tm_mon
	user_year = user_time.split()[-1]
	user_date = datetime(int(user_year), int(user_month), int(user_day))

	tweet_day = tweet_time.split()[2]
	tweet_month = strptime(tweet_time.split()[1],'%b').tm_mon
	tweet_year = tweet_time.split()[-1]
	tweet_date = datetime(int(tweet_year), int(tweet_month), int(tweet_day))

	difference = relativedelta.relativedelta(tweet_date, user_date)
	
	return difference.months
############################################################

############################################################
# Initializations
topics = ['charliehebdo', 'ferguson', 'germanwings-crash', 'ottawashooting', 'sydneysiege']

# Change this before running
base_dir = "/mnt/c/Users/Akshat/Desktop/Drive/Spring '19/Courses - Spring '19/Data Analytics Pipeline/Project/"
############################################################

for topic in topics:

	data_folder = os.path.join(base_dir, 'data', 'phemernrdataset', 'pheme-rnr-dataset')
	topic_folder = os.path.join(data_folder, topic)

	rumours = glob(topic_folder + '/rumours/**/**/*.json', recursive=True)
	non_rumours = glob(topic_folder + '/non-rumours/**/**/*.json', recursive=True)

	# Mimic database table Tweets
	labels = [	'tweet_id', 'tweet_hashtag', 'tweet_text', 
				'retweet', 'retweet_source_id', 'retweet_count', 'is_fake',
				'user_verified', 'user_followers_count', 'user_statuses_count',
				'user_friends_count', 'user_favourites_count', 'tweet_relative_age']

	data_list_fake = set()
	data_list_non_fake = set()

	for file in rumours:
	    with open(file) as json_file:
	        d = json.load(json_file)
	        tweet_id = str(d['id'])
	        hashtag = topic
	        text = d['text']
	        text = text.replace('\r', ' ')
	        if d['retweeted'] == False:
	            retweeted = 'false'
	        else:
	            retweeted = 'true'
	        in_reply_to = str(d['in_reply_to_status_id'])
	        retweet_count = int(d['retweet_count'])
	        is_fake = 'true'
	        user_verified = d['user']['verified']
	        user_followers_count = d['user']['followers_count']
	        user_statuses_count = d['user']['statuses_count']
	        user_friends_count = d['user']['friends_count']
	        user_favourites_count = d['user']['favourites_count']
	        user_created_at = d['user']['created_at']
	        tweet_created_at = d['created_at']
	        tweet_relative_age = tweet_age(user_created_at, tweet_created_at)
	        data_list_fake.add(tuple([tweet_id, hashtag, text, retweeted, in_reply_to, retweet_count, is_fake, user_verified, 
	        							user_followers_count, user_statuses_count, user_friends_count, user_favourites_count, tweet_relative_age]))

	for file in non_rumours:
	    with open(file) as json_file:
	        d = json.load(json_file)
	        tweet_id = str(d['id'])
	        hashtag = topic
	        text = d['text']
	        text = text.replace('\r', ' ')
	        if d['retweeted'] == False:
	            retweeted = 'false'
	        else:
	            retweeted = 'true'
	        in_reply_to = str(d['in_reply_to_status_id'])
	        retweet_count = int(d['retweet_count'])
	        is_fake = 'false'
	       	user_verified = d['user']['verified']
	        user_followers_count = d['user']['followers_count']
	        user_statuses_count = d['user']['statuses_count']
	        user_friends_count = d['user']['friends_count']
	        user_favourites_count = d['user']['favourites_count']
	        user_created_at = d['user']['created_at']
	        tweet_created_at = d['created_at']
	        tweet_relative_age = tweet_age(user_created_at, tweet_created_at)
	        data_list_non_fake.add(tuple([tweet_id, hashtag, text, retweeted, in_reply_to, retweet_count, is_fake, user_verified, 
	        								user_followers_count, user_statuses_count, user_friends_count, user_favourites_count, tweet_relative_age]))


	all_tweets = list(data_list_fake) + list(data_list_non_fake)


	df = pd.DataFrame.from_records(all_tweets, columns=labels)

	# write to csv
	csv_name  = topic + '_tweets.csv'
	save_location = os.path.join(base_dir, 'data')
	
	df.to_csv(os.path.join(save_location, csv_name), index=False)

	print("{} saved".format(topic))
