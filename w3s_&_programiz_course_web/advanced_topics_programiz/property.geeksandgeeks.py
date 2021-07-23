"""
A property object has three methods, getter(), setter(), and delete(). 

property() function in Python has four arguments property(fget, fset, fdel, doc), 
- fget is a function for retrieving an attribute value.
- fset is a function for setting an attribute value.
- fdel is a function for deleting an attribute value. doc creates a docstring for attribute.

A property object(any name) has three methods, getter(), setter(), and delete()
to specify fget, fset and fdel individually.


>>>

"""
@property
def x(self):
    return self._x

is equivalent to

def getx(self):
    return self._x
x = property(getx) # the property function



@property #is a getter function

@name.setter #is the setter