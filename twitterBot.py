# todo: tweet every time it goes up 1%
	# congrats message 
	# visual progress bar

from datetime import date
import sys

# shoutout: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
def progress(count, total):
    bar_len = 30
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    print('[%s] %s%s \r' % (bar, percents, '%'))


firstDay = date(2017, 9, 5)
lastDay = date(2021, 4, 29)

birth = date(1999, 9, 28)

today = date.today() 

delta = lastDay - today
daysSinceStart = today - firstDay
totalDaysOfUndergrad = lastDay - firstDay
daysAlive = today - birth

print("Total days  being alive: ", daysAlive.days)
print("Total days of undergrad: ", totalDaysOfUndergrad.days)
print("Days since school start: ", daysSinceStart.days)
print("Days till school finish: ", delta.days)
print()

symbol = " % "
percentSchool = float((daysSinceStart.days/daysAlive.days)*100)
print("%1.f%s of life spent in undergrad" % (percentSchool, "%"))

print()
print("Undergrad progress: ", end='')
percent = float((daysSinceStart.days/totalDaysOfUndergrad.days)*100)

progress(percent,100);