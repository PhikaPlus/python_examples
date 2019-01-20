import datetime

print(20*'-')
today = datetime.datetime.today()
now = datetime.datetime.now()
y = now.year
m = now.month
d = now.day
utc_time = datetime.datetime.utcnow()
print(today)
print(now)
print(utc_time)
print(y, m, d)

# ------------------------------------------------------------
print(20*'-')
# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
print(now.year)
print('today is:', now.strftime("%A"))

# ------------------------------------------------------------
print(20*'-')
# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
my_birthday = datetime.date(1991, 5, 1)
x = datetime.datetime(2020, 5, 17)
my_birthday2 = datetime.datetime(1991, 5, 1, 9, 15, 38)
event_date = datetime.date(2018, 8, 3)
event_date_and_time = datetime.datetime(2018, 8, 3, 15, 16, 36)
print(my_birthday)
print(x)
print(event_date)
print(event_date - my_birthday)
print(event_date_and_time)
print(event_date_and_time - my_birthday2)

