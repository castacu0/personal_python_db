import datetime as dt

dtX = dt.datetime.now()
print(dtX)
"""
Commonly used classes in the datetime module are:

- date Class
- time Class
- datetime Class
    # The datetime class contains 
    # >>> year, month, day,   hour, minute, second, and microsecond (tzone=None)
- timedelta Class
"""
#strftime() and strptime()

print(dtX.strftime("%A")) # Weekday, full version
print(dtX.strftime("%H")) # Hour 00-23
print(dtX.strftime("%j")) # Day number of year 001-366

>>>pytZ module
for handling timezones in a easier way


# Just in case: https://www.w3schools.com/python/python_datetime.asp 