"""There are 3 ways of writing a 'except' block:

1-. except:

2-. except ______:

3-. except ______ as variable:

"""
try:
    #something = 10/0    #possible line to throw the 3rd case error
    givenNum = int(input("Give me a num: "))
    print(givenNum)

# except: #Fuc* this one. Don't use it
#     print ("Very basic error, We!")

except ValueError: #2nd case, expecifying the error
    print("Wrong Input.")

except ZeroDivisionError as err: #3rd case. Storing the value inside of err
    print(f"This is the original error {err}")