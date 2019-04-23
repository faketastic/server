import pandas as pd
import os.path
import json

dir = os.path.dirname(os.path.abspath(__file__))
# data_folder = os.path.join(dir, '..', '..')
# data_folder = '..\\..\\data\\subset\\charliehebdo'
data_folder = os.path.join(dir, 'subset', 'charliehebdo')
rumours = os.path.join(data_folder, 'rumours')
non_rumours = os.path.join(data_folder, 'non-rumours')
# curr_file = os.path.join(rumours, '552943855021330432.json')
dat = dict()

with open(curr_file) as json_file:
    data = json.load(json_file)
    dat['id'] = data['id_str']
    dat['text'] = data['text']
    dat['in_reply_to_status_id'] = data['in_reply_to_status_id_str']
    dat['retweeted'] = data['retweeted']
    dat['retweet_count'] = data['retweet_count']

print dat
