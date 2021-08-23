# Initialize the list
my_list = [1, 3, 6, 10]
# square each term using list comprehension
list_ = [x**2 for x in my_list]
# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)
print(list_) # [1, 9, 36, 100]
print(generator) # <generator object <genexpr> at 0x7f5d4eb4bf50>

# It returned a generator object, which produces items only on demand.
# This should do the thing now
g = (x**2 for x in my_list)
print(next(g))
print(next(g))


""" 
Generator expressions can be used as function arguments/parameters.
 When used in such a way, the round parentheses can be dropped.
 
 >>> sum(x**2 for x in my_list)
146

>>> max(x**2 for x in my_list)
100
"""