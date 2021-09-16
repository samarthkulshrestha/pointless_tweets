import time

import tweepy

from keys import *
from phrases import Sentence

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

tw = Sentence()
api.update_status(tw)
print(tw)
