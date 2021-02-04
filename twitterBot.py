from datetime import date
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
def progressBar(count, total):
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '|' * filled_len + '-' * (bar_len - filled_len)
    return ('[%s] %s%s \r' % (bar, percents, '%'))


def summary():
    firstDay = date(2017, 9, 5)
    lastDay = date(2021, 4, 29)
    birth = date(1999, 9, 28)
    today = date.today()

    daysAlive = today - birth
    totalDaysOfUndergrad = lastDay - firstDay
    daysSinceStart = today - firstDay

    progress = progressBar(calculateProgress(), 100)
    percentSchool = float((daysSinceStart.days/daysAlive.days)*100)
    summaryTweet = "Now that @alexreyes243 is done with college, here's a summary: \n\nTotal days being alive: %d\nTotal days of undergrad: %d\nTotal %s of life in undergrad: %1.f%s 😱\n\nTotal times he considered dropping out: ∞\n\n%s" % (daysAlive.days, totalDaysOfUndergrad.days, "%", percentSchool, "%", progress)

    return summaryTweet


def calculateProgress():
    firstDay = date(2017, 9, 5)
    lastDay = date(2021, 4, 29)
    today = date.today()

    totalDaysOfUndergrad = lastDay - firstDay
    daysSinceStart = today - firstDay

    percent = float((daysSinceStart.days/totalDaysOfUndergrad.days)*100)

    return percent


def main():
    progressPercent = calculateProgress()
    summaryTweet = summary()
    progress = progressBar(progressPercent, 100)

    roundedProgress = (round(progressPercent, 1))

    if (roundedProgress == 100):
        print("Sending final 100% tweet!")
        send_tweet("@alexreyes243 is officially a Penn State graduate 🎓 🎉 🥳")
        send_tweet(summaryTweet)

    elif (roundedProgress > 100):
        print("Already done with this bot account!")
        exit()

    elif(roundedProgress.is_integer()):
        print("Sending progress tweet")

        print(progress)
        send_tweet(progress)

    else:
        print("No tweet today. Progress: %f" % (roundedProgress))


main()
