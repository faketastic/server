import pandas as pd
import os.path
import json


# Mimic database table Tweets
labels = ['tweet_id', 'tweet_hashtag', 'tweet_text', 'retweet',
          'retweet_source_id', 'retweet_count', 'is_fake']

base_dir = '/home/eric/FakeTastic/server'
data_folder = os.path.join(base_dir, 'pheme-rnr-dataset')

# Get all hashtags
hashtags = os.listdir(data_folder)
hashtags.remove('README')

# Initialize data lists
data_list_fake = []
data_list_non_fake = []

# Iterate over hashtags
for hashtag in hashtags:
    hashtag_folder = os.path.join(data_folder, hashtag)
    rumours = os.path.join(hashtag_folder, 'rumours')
    non_rumours = os.path.join(hashtag_folder, 'non-rumours')

    # Iterate over tweets
    for tweet_folder in os.listdir(rumours):
        # Get path for source tweet
        curr_folder = os.path.join(rumours, tweet_folder, 'source-tweet')
        file_name = os.listdir(curr_folder)[0]
        curr_file = os.path.join(curr_folder, file_name)
        
        with open(curr_file) as f:
            d = json.load(f)
            tweet_id = d['id_str']
            text = d['text'].replace('"', '')
            if d['retweeted'] == False:
                retweeted = 'false'
            else:
                retweeted = 'true'
            in_reply_to = d['in_reply_to_status_id_str']
            retweet_count = int(d['retweet_count'])
            is_fake = 'true'
            if tweet_id == '499401831874043905':
                pass
            else:
                data_list_fake.append([tweet_id, hashtag, text, retweeted,
                                       in_reply_to, retweet_count, is_fake])

    # Iterate over tweets
    for tweet_folder in os.listdir(non_rumours):
        # Get path for source tweet
        curr_folder = os.path.join(non_rumours, tweet_folder, 'source-tweet')
        file_name = os.listdir(curr_folder)[0]
        curr_file = os.path.join(curr_folder, file_name)
        
        with open(curr_file) as f:
            d = json.load(f)
            tweet_id = d['id_str']
            text = d['text'].replace('"', '\"')
            if d['retweeted'] == False:
                retweeted = 'false'
            else:
                retweeted = 'true'
            in_reply_to = d['in_reply_to_status_id_str']
            retweet_count = int(d['retweet_count'])
            is_fake = 'false'
            if tweet_id == '499401831874043905':
                pass
            else:
                data_list_non_fake.append([tweet_id, hashtag, text, retweeted,
                                       in_reply_to, retweet_count, is_fake])


all_tweets = data_list_fake + data_list_non_fake

df = pd.DataFrame.from_records(all_tweets, columns=labels)

# Write to csv
df.to_csv(os.path.join(base_dir, 'tweets.csv'), index=False)
