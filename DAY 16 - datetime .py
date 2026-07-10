from datetime import datetime
from datetime import date
from datetime import time

###💻 Exercises: Day 16
#Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month              
year = now.year          
hour = now.hour                 
minute = now.minute           
timestamp = now.timestamp()
print(f'{day}/{month}/{year}, {hour}:{minute}, {timestamp}')

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)

#Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y") #%B is the month in full, and %Y is year in full
print(date_object)

#Calculate the time difference between now and new year.
t1 = datetime.now()
t2 = datetime(2027, 1, 1)
print(t2-t1)

#Calculate the time difference between 1 January 1970 and now.
t1 = datetime.now()
t2 = datetime(1970, 1, 1)
print(t1-t2)