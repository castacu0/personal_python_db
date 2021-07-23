# We have to remember that @property is a decorator
# A decorator function is a modifier for anoter function
# It commonly adds some extra lines of code to it.
#
# Getters and setters are used in many object-oriented programming
# languages to ensure the principle of data encapsulation:

#   These methods are of course the getter for retrieving the data
#   and the setter for changing the data.

# According to this principle, the attributes of a class are made _private
# to hide and protect them from other codes.

@property is basically a pythonic way to use getters and setters.

"""
Getter: It will be in charge of getting the value of an attribute >>> reading. (get = get)

Setter: It is responsible for intercepting when >>> typing. (set = set(definir) or write)

Deleter: It is responsible for intercepting when it is >>> deleted. (delete = delete)

doc: You will receive a string to document the attribute. (doc = documentation)


🍁 Getters and Setters are also known as 'Accessor' methods
    - Getters are called Accessors
    - Setters as Mutators





Two ways to do it according to the documentation 

>>> property() function
and
>>> @property decorator
"""

