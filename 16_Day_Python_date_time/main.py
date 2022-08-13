from datetime import datetime
from datetime import date

##Get the current day, month, year, hour, minute and timestamp from datetime module

now = datetime.now()
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.hour)
# print(now.minute)
# timestamp = now.timestamp()
# print(timestamp)

##Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

time_one = now.strftime("%m/%d/%Y, %H:%M:%S")

##Today is 5 December, 2019. Change this time string to time.

string = 'Today is 5 December, 2019'
string = string.split(' ')[2:]
string = " ".join(map(str, string))
date_object = datetime.strptime(string, "%d %B, %Y")
# print("date_object =", date_object)

##Calculate the time difference between now and new year.

now = datetime.now()
now = now.strftime("%Y-%m-%d").split('-')

now = list(map(int, now))


now = date(year=now[0], month=now[1], day=now[2])
new_year = date(year=2023, month=1, day=1)
print(new_year)
time_left_for_newyear = new_year - now
print(time_left_for_newyear)