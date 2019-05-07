---------------------------------
-----Faketastic Database DDL-----
---------------------------------

-- Tweets table
DROP TABLE IF EXISTS Tweets;
CREATE TABLE Tweets
(
  tweet_id              TEXT PRIMARY KEY,
  tweet_hashtag         TEXT NOT NULL,
  tweet_text            TEXT NOT NULL,
  retweet               BOOLEAN NOT NULL,
  retweet_source_id     TEXT,
  retweet_count         INTEGER,
  is_fake               BOOLEAN,
  user_verified         BOOLEAN, 
  user_followers_count  INTEGER, 
  user_statuses_count   INTEGER, 
  user_friends_count    INTEGER, 
  user_favourites_count INTEGER, 
  tweet_relative_age    INTEGER
);

-- Response table
DROP TABLE IF EXISTS Response;
CREATE TABLE Response
(
  response_id  SERIAL PRIMARY KEY,
  tweet_id     TEXT NOT NULL,
  is_fake      BOOLEAN NOT NULL,
  CONSTRAINT response_tweet_id_fk
  FOREIGN KEY (tweet_id)
  REFERENCES Tweets (tweet_id) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Topics table
DROP TABLE IF EXISTS Hashtags;
CREATE TABLE Hashtags
(
  hashtag_id    SERIAL PRIMARY KEY,
  tweet_hashtag TEXT NOT NULL
);