"""
https://jfine-python-classes.readthedocs.io/en/latest/property-from-class.html  

A property is a way of providing a class with virtual or protected attributes.
They can be a good way of hiding and protecting implementation details. 

/ Some properties are both read and write.
/ There may also be a case for write-only properties.
/ One can also delete a property. 
/ To help the programmer, a property can have a docstring.

The signature for property is:

property(fget=None, fset=None, fdel=None, doc=None)


Let's start with Python decorators.

A Python decorator is a function that helps to add some additional functionalities to an already defined function.

In Python, everything is an object. Functions in Python are first-class objects which means that they can be referenced by a variable, added in the lists, passed as arguments to another function etc.

Consider the following code snippet.

def decorator_func(fun):
    def wrapper_func():
        print("Wrapper function started")
        fun()
        print("Given function decorated")
        # Wrapper function add something to the passed function and decorator 
        # returns the wrapper function
    return wrapper_func

def say_bye():
    print("bye!!")

say_bye = decorator_func(say_bye)
say_bye()

# Output:
#  Wrapper function started
#  bye
#  Given function decorated
Here, we can say that decorator function modified our say_hello function and added some extra lines of code in it.

Python syntax for decorator

def decorator_func(fun):
    def wrapper_func():
        print("Wrapper function started")
        fun()
        print("Given function decorated")
        # Wrapper function add something to the passed function and decorator 
        # returns the wrapper function
    return wrapper_func

@decorator_func
def say_bye():
    print("bye!!")

say_bye()
Let's Concluded everything than with a case scenario, but before that let's talk about some oops priniciples.

Getters and setters are used in many object oriented programming languages to ensure the principle of data encapsulation(is seen as the bundling of data with the methods that operate on these data.)

These methods are of course the getter for retrieving the data and the setter for changing the data.
"""