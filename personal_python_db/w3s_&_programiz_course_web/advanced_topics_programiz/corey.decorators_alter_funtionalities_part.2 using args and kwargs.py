"""
The proper way to never forget how decorators work is just
keeping in mind what that '@' syntax means: 

@decorator
    def function():
    ...

is equivalent to: exit_function = decorator(function).

@decorator_function 
    def display():

displayX = decorator_function(display)
"""

# PART 2
# OK, CAREFUL HERE
# Now we are using   >>> *args and **kwargs

# We are decorating 2 def functions
# Alse, we are now passing several param/args to our wrapper inside of the main decorator_function

def decorator_function(func_to_alter):
    def wrapper_function(*args, **kwargs): #this is the one that will receieve the param/args
        print(f"Wrapper running b4 func_to_alter named '{func_to_alter.__name__}'")
        # .__name__ helps to know who or what is the argument being passed as param
        return func_to_alter(*args,**kwargs) 
               # the function that is being decorated might have params, so let's prevent any error
               # def person(name, age) for example, has 2
    return wrapper_function #call me pls

@decorator_function 
                    # this works cause display has no params
def display(): 
    print("Decorator Working for me! I'm DISPLAY")
display() #no arg

@decorator_function # this decorator would work with 'def person' if I don't put the *args and **kwargs
                    # inside of the wrapper and inside of the caller of the 'return func_to_alter()'
def person(name, age):
    print(f"Function 'person' working with param/args: ({name}, {age})")
person('Cesar', 21) #caller with 2 args