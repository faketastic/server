---------------------------------
-----Faketastic Database DDL-----
---------------------------------

-- Tweets table
DROP TABLE IF EXISTS Tweets;
CREATE TABLE Tweets
(
  tweet_id          TEXT PRIMARY KEY,
  tweet_hashtag     TEXT NOT NULL,
  tweet_text        TEXT NOT NULL,
  retweet           BOOLEAN NOT NULL,
  retweet_source_id TEXT,
  retweet_count     INTEGER,
  is_fake           BOOLEAN
);

-- Response table
DROP TABLE IF EXISTS Response;
CREATE TABLE Response
(
  response_id  SERIAL PRIMARY KEY,
  tweet_id     INTEGER NOT NULL,
  is_fake      BOOLEAN NOT NULL,
  CONSTRAINT response_tweet_id_fk
  FOREIGN KEY (tweet_id)
  REFERENCES Tweets (tweet_id) MATCH SIMPLE
  ON UPDATE NO ACTION ON DELETE NO ACTION,
);

-- User table
-- DROP TABLE IF EXISTS Users;
-- CREATE TABLE Users
-- (
--   userid            INTEGER,
--   username          TEXT,
--   response_tweetid  TEXT,
--   game_response     INTEGER
-- )
-- PRIMARY KEY (userid)
-- FOREIGN KEY (response_tweetid) REFERENCES Tweets(tweetid);
