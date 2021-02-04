# todo: tweet every time it goes up 1%
# congrats message
		# summary message  

from datetime import date
import sys
import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

def send_tweet(tweet):
	auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
	auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
	api = tweepy.API(auth)

	api.update_status(tweet)


# shoutout: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '|' * filled_len + '-' * (bar_len - filled_len)
    return ('[%s] %s%s \r' % (bar, percents, '%'))

def calculateProgress():
	firstDay = date(2017, 9, 5)
	lastDay = date(2021, 4, 29)
	birth = date(1999, 9, 28)
	today = date.today() 

	daysAlive = today - birth
	totalDaysOfUndergrad = lastDay - firstDay
	daysSinceStart = today - firstDay
	daysLeft = lastDay - today

	print("Total days  being alive: ", daysAlive.days)
	print("Total days of undergrad: ", totalDaysOfUndergrad.days)
	print("Days since school start: ", daysSinceStart.days)
	print("Days till school finish: ", daysLeft.days)
	print()

	symbol = " % "
	percentSchool = float((daysSinceStart.days/daysAlive.days)*100)
	print("%1.f%s of life spent in undergrad 😱" % (percentSchool, "%"))

	print()
	# print("Undergrad progress: ", end='')
	percent = float((daysSinceStart.days/totalDaysOfUndergrad.days)*100)

	return percent

def main(): 
	percent = calculateProgress()
	progressBar = progress(percent,100)

	print(progressBar)
	# send_tweet(progressBar)

main()