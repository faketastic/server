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

