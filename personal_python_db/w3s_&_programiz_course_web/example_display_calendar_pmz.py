#Display Calendar
import calendar

user_yyyy = int(input("Enter year (4 ints): "))
user_mm = int(input("Enter month (2 ints): "))

print(calendar.month(user_yyyy, user_mm)) # 2021 05
#   module👆   👆function  👆 params and args


"""
May 2021      
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
"""