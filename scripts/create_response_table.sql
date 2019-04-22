CREATE TABLE response (
 response_id serial PRIMARY KEY, 
 tweet_id integer NOT NULL ,
 is_fake boolean NOT NULL,
  CONSTRAINT response_tweet_id_fk FOREIGN KEY (tweet_id)
      REFERENCES tweet (tweet_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION,
)
