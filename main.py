import tweepy
import schedule
import time

CONSUMER_KEY ="(CONSUMER_KEY)"
CONSUMER_SECRET = "(CONSUMER_SECRET)"
ACCESS_KEY = "(ACCESS_KEY)"
ACCESS_SECRET = "(ACCESS_SECRET)"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
number = 0
def tweet():
    global number
    api.update_status('Please @snapchat, undo your update ! #' + str(number))
    int(number)
    number+=1

schedule.every(20).minutes.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
