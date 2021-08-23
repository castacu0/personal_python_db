def imthedecorator(parameter):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
      # return divide(2, 5)
        return parameter(a, b)
    return inner #im calling this function with the return not with its ()


@imthedecorator #parameter
# This 👇 is the function I want to decorate 
def divide(a, b):
    print(a/b)

divide(2,5)
divide(2,0)

"""
we can make general decorators that work with any number of parameters.

In Python, this magic is done as function(*args, **kwargs). In this way,
args will be the tuple of positional arguments and kwargs will be the
dictionary of keyword arguments.

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner
"""