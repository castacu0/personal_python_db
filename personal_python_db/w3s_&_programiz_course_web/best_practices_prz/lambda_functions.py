# ⭐ Example 1 ⭐
# A normal function compared to a lambda

# def cubic(n):
#     return n * 2

cubic = lambda n: n ** 3
print(cubic(5))



# ⭐ Example 2 ⭐ 
# With 2 parameterss and a condition

larger = lambda a, b: a  if a > b  else b
print(larger(10, 47))



# ⭐ Example 3 ⭐ 
# lambda functions as keys to < sort() >

names = ['Alan', 'Gregory', 'Zlatan', 'Jonas', 'Tom', 'Bugustine']

names.sort() #Let's sort this list alphabetically A-Z
print(names)

names.sort(key = lambda x0: len(x0))
# We're passing an optional 'key' argument to the sort() method.
# And then, running a function without declaring it
print(names)


# ['Alan', 'Augustine', 'Gregory', 'Jonas', 'Tom', 'Zlatan']
# ['Tom', 'Alan', 'Jonas', 'Zlatan', 'Gregory', 'Augustine']