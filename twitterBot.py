# todo: tweet every time it goes up 1%
	# congrats message 
	# visual progress bar

from datetime import date

firstDay = date(2017, 8, 21)
lastDay = date(2021, 5, 7)

today = date.today() 

delta = lastDay - today
daysSinceStart = today - firstDay
totalDaysOfUndergrad = lastDay - firstDay

print("Total days since school started: ", daysSinceStart.days)
print("Days till finish: ", delta.days)
print("Total days of undergrad: ", totalDaysOfUndergrad.days)


percent = float((daysSinceStart.days/totalDaysOfUndergrad.days)*100)
print("Progress: %.1f" % (percent) + "%")