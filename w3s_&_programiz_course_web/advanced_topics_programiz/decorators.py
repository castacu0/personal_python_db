"""
"A decorator is just a function that takes another function as an
argument, adds some kind of functionality, and then returns another function."


So, in the most basic sense, a decorator is a callable, that takes a callable
and returns a callable.

"""
def make_pretty(parameter):
    def inner():
        print("I got decorated")
        parameter() #ordinary gets here  #I'm accepting a func and calling it()
    return inner

@make_pretty #the parameter is not needed to be called
def ordinary():
    print("I am ordinary function")

ordinary() #but this has

