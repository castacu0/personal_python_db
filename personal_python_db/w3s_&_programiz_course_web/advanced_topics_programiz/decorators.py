"""
"A decorator is just a function that takes another function as an
argument, adds some kind of functionality, and then returns another function."

"""
def decorator_function(func_to_alter):
    def wrapper():
        print("I got decorated")
        return func_to_alter() #now calling the ordinary()
        #func_to_alter() #same shit
    return wrapper

@decorator_function #decorate this 👇 please
def ordinary():
    print("I am an ordinary function")

ordinary() #but this is calling the wrapper  >>> ()

