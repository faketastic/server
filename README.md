## Faketastic
### Data Analytics Pipelines Spring 2019
FakeTastic is a web browser game in which players guess whether or not they think tweets are *real* or *fake*. First, players select a tweet hashtag and then they are able to place their guesses for a set of 10 tweets. We mark responses as *correct* or *incorrect* and show the player immediately.

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

For now, #charliehebdo is the only topic populated with tweets so go ahead and select it and click *View*.  

![Topic selection](https://github.com/faketastic/server/blob/master/assets/select_topic.png "Topic selection")
### Members
Ankita Agrawal, Eric Boxer, Akshat Mittal, Andrea Navarrete Rivera, Harin Sanghirunm
