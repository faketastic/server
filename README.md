## Faketastic

### Members
Ankita Agrawal aa4229, Eric Boxer ecb2198, Akshat Mittal am5022, Andrea Navarrete Rivera an2886, Harin Sanghirun hs3058

### Data Analytics Pipelines Spring 2019
FakeTastic is a web browser game in which players guess whether or not they think tweets are *real* or *fake*. First, players select a tweet hashtag and then they are able to place their guesses for a set of 10 tweets. We mark responses as *correct* or *incorrect* and show the player immediately.

### Web address
[FakeTastic](http://3.82.127.96:8111/)

### Instructions for running locally
Clone the server directory.  

```
git clone https://github.com/faketastic/server.git
```

Enter the server directory.  

```
cd server
```

Activate your virtual environment and then pip install requirements.  

```python 
pip install -r requirements.txt 
```

Run `server.py`.  

```python
python server.py
```

Now you can access the application in your browser, navigate to localhost:8111.  

![Run the server](https://github.com/faketastic/server/blob/master/assets/run_server.png "Run the server")

For now, #charliehebdo is the only topic populated with tweets, so go ahead and select it and then click *View*.  

![Topic selection](https://github.com/faketastic/server/blob/master/assets/select_topic.png "Topic selection")

Now you can see the text from ten tweets from the hashtag #ferguson.  

![Tweet display](https://github.com/faketastic/server/blob/master/assets/before.png "Tweet display")

Which do you think are fake? Go ahead and mark those that don't seem real.  
When you've made your guesses, click submit to have your responses scored.  
The *Grade* column displays a check for each correct response. The *Prediction Confidence* column displays the predicted probabilities from our model - the fuller the bar, the more confident we are of our prediction. A red bar corresponds to a fake tweet and a green corresponds to a not fake tweet.

![Response scoring](https://github.com/faketastic/server/blob/master/assets/after.png "Response scoring") 

Responses are stored in our database, for user analytics and for retraining a yet to be implemented fake tweet detection machine learning model.  

![Response database](https://github.com/faketastic/server/blob/master/assets/response_database.png "Response database") 

### Resources
[Jira](https://toydemoproject.atlassian.net/jira/software/projects/FAK/boards/10)
