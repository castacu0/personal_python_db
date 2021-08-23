# #Leap Year
# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year

year = int(input("Write a num: ")) #it's a century one

#only divisible by 400
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a gap year.")
        else:
            print(f"{year} is NOT a gap year. 3rd IF")
    else:
        print(f"{year} is a gap year. 2nd IF")
else:
    print(f"{year} is NOT a gap year. 1st IF")
