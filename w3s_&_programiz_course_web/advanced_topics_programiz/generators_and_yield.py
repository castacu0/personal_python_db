#import time
#programiz
""" 
Both yield and return will return some value from a function.

The difference is that while a return statement terminates a
function entirely, yield statement pauses the function saving
all its states and later continues from there on successive calls.



One interesting thing to note is that the value
of variable n is remembered between each call *(website example).

Unlike normal functions, the local variables are not destroyed when the function yields.
"""


"""Methods like __iter__() and __next__() are implemented automatically. 
SOOOO we can iterate through the items using      <next()>.

StopIteration is raised automatically on further calls."""


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
# We have to call the lazy Generator if we want to see the value



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




# ⭐ WAY 4: Pipelining Gens ⭐
# 0, 1,   1, 2, 3, 5, 8, 13, 21, 34
print("\n")

def fibonacci_numbers(nums): #10  /  from 0 to 9
    x, y = 0, 1 # base case
    for fib in range(nums):
        x, y = y, x + y
        #x with y  &  y with x+y
        yield x

def square(nums):
    for i in nums:
        yield i**2

print(sum(square(fibonacci_numbers(10))))
# 4895


"""
They have lazy execution ( producing items only when asked for ). For this reason,
 a generator expression is much more memory efficient than an equivalent list comprehension.
"""