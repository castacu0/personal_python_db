#import time
""" 
Both yield and return will return some value from a function.

The difference is that while a return statement terminates a
function entirely, yield statement pauses the function saving
all its states and later continues from there on successive calls.
"""


# ⭐ WAY 1: Activating the Generator ⭐
# 1st, we started setting up a function, then we used a for loop
# to iterate that function, after that we used the explicit "next" command
# to access the Generator saved inside of "var". 
def funct(param = 1):
    while True:  # while True: means this loop is gonna continue indefinitely
        yield param  # return and let it continue
        param += 1

var = funct()
for i in range(10):
    print(next(var), end=' ') #No need to use NEXT several times
    #time.sleep(0.5)



# ⭐ WAY 2: Generators from Generator Expressions ⭐
# Similar to List Comprehension, but uses () rather than []
print("\n")
generator = (traveler for traveler in range(1000000))
print(next(generator))
next(generator)
print(next(generator))



# ⭐ WAY 3: Generator to Read File⭐
#https://github.com/joeyajames/Python/blob/master/Python%20Generators.ipynb
print("\n")
def read_file(document = 'bandsX.txt'):
    for each_line in open(document):
        yield each_line
  
obj = read_file()
# print(next(obj))
for i in range(6):
    print(next(obj), end='')