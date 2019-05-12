#!/usr/bin/env python3.6

"""
COMS W4995 Data Analytics Pipelines
FakeTastic webserver

To run locally

    python server.py

Go to http://localhost:8111 in your browser
"""

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response
import numpy as np
from model import get_model

import credentials
import json

import json as json


tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
app.config['TEMPLATES_AUTO_RELOAD'] = True




# XXX: The Database URI should be in the format of: 
#
#     postgresql://USER:PASSWORD@<IP_OF_POSTGRE_SQL_SERVER>/<DB_NAME>
#
# For example, if you had username ewu2493, password foobar, then the following line would be:
#
#     DATABASEURI = "postgresql://ewu2493:foobar@<IP_OF_POSTGRE_SQL_SERVER>/postgres"
#
# For your convenience, we already set it to the class database

# Use the DB credentials you received by e-mail
# DB_USER = "YOUR_DB_"
# DB_PASSWORD = "YOUR_DB_PASSWORD_HERE"
DB_USER = credentials.username()
DB_PASSWORD = credentials.password()

# DB_SERVER = "w4111.cisxo09blonu.us-east-1.rds.amazonaws.com"
DB_SERVER = "mydbinstance.cmgiyjltohsu.us-east-1.rds.amazonaws.com"

# DATABASEURI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_SERVER+"/w4111"
DATABASEURI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@"+DB_SERVER+"/FakeTasticdb"

#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)


# Here we create a test table and insert some values in it
engine.execute("""DROP TABLE IF EXISTS test;""")
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id serial,
  name text
);""")
engine.execute("""INSERT INTO test(name) VALUES ('grace hopper'), ('alan turing'), ('ada lovelace');""")

model = get_model()

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request

  The variable g is globally accessible
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None


@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


#@app.route('/')
#def index():
#  """
#  request is a special object that Flask provides to access web request information:
#
#  request.method:   "GET" or "POST"
#  request.form:     if the browser submitted a form, this contains the data in the form
#  request.args:     dictionary of URL arguments e.g., {a:1, b:2} for http://localhost?a=1&b=2
#
#  See its API: http://flask.pocoo.org/docs/0.10/api/#incoming-request-data
#  """
#
#  # DEBUG: this is debugging code to see what request looks like
#  print(request.args)
#
#
#  #
#  # example of a database query
#  #
#  cursor = g.conn.execute("SELECT name FROM test")
#  names = []
#  for result in cursor:
#    names.append(result['name'])  # can also be accessed using result[0]
#  cursor.close()
#
#  #
#  # Flask uses Jinja templates, which is an extension to HTML where you can
#  # pass data to a template and dynamically generate HTML based on the data
#  # (you can think of it as simple PHP)
#  # documentation: https://realpython.com/blog/python/primer-on-jinja-templating/
#  #
#  # You can see an example template in templates/index.html
#  #
#  # context are the variables that are passed to the template.
#  # for example, "data" key in the context variable defined below will be 
#  # accessible as a variable in index.html:
#  #
#  #     # will print: [u'grace hopper', u'alan turing', u'ada lovelace']
#  #     <div>{{data}}</div>
#  #     
#  #     # creates a <div> tag for each element in data
#  #     # will print: 
#  #     #
#  #     #   <div>grace hopper</div>
#  #     #   <div>alan turing</div>
#  #     #   <div>ada lovelace</div>
#  #     #
#  #     {% for n in data %}
#  #     <div>{{n}}</div>
#  #     {% endfor %}
#  #
#  context = dict(data = names)
#
#
#  #
#  # render_template looks in the templates/ folder for files.
#  # for example, the below file reads template/index.html
#  #
#  return render_template("index.html", **context)

#
# This is an example of a different path.  You can see it at
# 
#     localhost:8111/another
#
# notice that the functio name is another() rather than index()
# the functions for each app.route needs to have different names
#
@app.route('/')
def landing():
    # Get list of all hashtags
    # from DB
    cmd = '''
            SELECT  *
            FROM    hashtags
          '''
    hashtag_cursor = g.conn.execute(text(cmd))
    hashtags = []
    for result in hashtag_cursor:
        hashtags.append(result[1])
    return render_template('home.html', hashtags=hashtags)


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  print(name)
  cmd = 'INSERT INTO test(name) VALUES (:name1), (:name2)';
  g.conn.execute(text(cmd), name1 = name, name2 = name);
  return redirect('/')


@app.route('/response', methods=['POST'])
def response_create():
  data = json.loads(request.data)
  print(data)
  cmd = 'INSERT INTO response(tweet_id, is_fake) VALUES '
  for answer in data:
    cmd += f"({answer['tweetId']}, {answer['answer']}),"
  cmd = cmd[:-1]
  print(cmd)
  g.conn.execute(text(cmd))
  return '{ "response": "ok" }'


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()


@app.route('/tweets',methods=['GET','POST'])
def tweets():
  topic = request.form['topic_id']
  # cmd = "(Select tweet_id,tweet_text,is_fake from Tweets where tweet_hashtag = :topic LIMIT 10) "
  cmd1 = "(Select tweet_id,tweet_text,is_fake from tweets_detailed where tweet_hashtag = :topic and is_fake=False LIMIT 10) "
  cmd2 = "UNION (Select tweet_id,tweet_text,is_fake from tweets_detailed where tweet_hashtag = :topic and is_fake=True LIMIT 10 )"
  cmd  = cmd1+cmd2
  # print(cmd)
  alltweets = g.conn.execute(text(cmd),topic=str(topic))


  data = [dict(tweet_id=result[0], is_fake=result[2], 
              tweet_text=result[1]) for result in alltweets]
  conf = model.predict_proba([datum['tweet_text'] for datum in data])
  for i, datum in enumerate(data):
    datum['conf'] = conf[i][1]

  data = data[:10]
  data_string = json.dumps(data)
  context = dict(data=data, data_string=data_string, topic=topic)
  return render_template('tweets.html', **context)


if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    """
    This function handles command line parameters.
    Run the server using

        python server.py

    Show the help text using

        python server.py --help

    """

    HOST, PORT = host, port
    print("running on %s:%d" % (HOST, PORT))
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
