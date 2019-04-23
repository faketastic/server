import pandas as pd
import os.path
import json

base_dir = '/home/akshat/PycharmProjects/FakeTastic'
data_folder1 = os.path.join(base_dir, 'data')
data_folder = os.path.join(data_folder1, 'subset', 'charliehebdo')
rumours = os.path.join(data_folder, 'rumours')
non_rumours = os.path.join(data_folder, 'non-rumours')
curr_file = os.path.join(rumours, '552943855021330432.json')

# print(os.listdir(non_rumours))

# Mimic database table Tweets
labels = ['tweet_id', 'tweet_hashtag', 'tweet_text', 'retweet', 'retweet_source_id', 'retweet_count', 'is_fake']

data_list_fake = []
data_list_non_fake = []

for file in os.listdir(rumours):
    curr_file = os.path.join(rumours, file)
    with open(curr_file) as json_file:
        d = json.load(json_file)
        id = d['id_str']
        hashtag = 'charliehebdo'
        text = d['text']
        if d['retweeted'] == False:
            retweeted = 'false'
        else:
            retweeted = 'true'
        in_reply_to = d['in_reply_to_status_id_str']
        retweet_count = int(d['retweet_count'])
        is_fake = 'true'
        data_list_fake.append([id, hashtag, text, retweeted, in_reply_to, retweet_count, is_fake])

for file in os.listdir(non_rumours):
    curr_file = os.path.join(non_rumours, file)
    with open(curr_file) as json_file:
        d = json.load(json_file)
        id = d['id_str']
        hashtag = 'charliehebdo'
        text = d['text']
        if d['retweeted'] == False:
            retweeted = 'false'
        else:
            retweeted = 'true'
        in_reply_to = d['in_reply_to_status_id_str']
        retweet_count = int(d['retweet_count'])
        is_fake = 'false'
        data_list_non_fake.append([id, hashtag, text, retweeted, in_reply_to, retweet_count, is_fake])

all_tweets = data_list_fake + data_list_non_fake

df = pd.DataFrame.from_records(all_tweets, columns=labels)

# write to csv
df.to_csv(os.path.join(data_folder1, 'tweets.csv'), index=False)
