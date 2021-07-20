# PART 3
# Now we are using a Class to replicate our def decorator_func

class decorator_class(): #exact same functionality as my 'def decorator_function(func_to_alter):'

    def __init__(self, func_to_alter): #this is the parameter, has to be inside of the __init__
        self.func_to_alterX = func_to_alter

      # __call__ helps us to mimic the wrapper behavior 
    def __call__(self, *args, **kwargs): # this is the WRAPPER
        print(f"Wrapper now is __call__ method: '{self.func_to_alterX.__name__}'") #Have to use 
        return self.func_to_alterX(*args, **kwargs) 
        # because we are returning a main parameter (func_to_alter), we have to ask __init__ 
        # for permission to use it so 'return self.func...'

# def decorator_function(func_to_alter):
#     def wrapper_function():
#         print(f"Wrapper running b4 func_to_alter named '{func_to_alter.__name__}'")
#         return func_to_alter() 
#     return wrapper_function

 
#@decorator_function
@decorator_class
def display(): 
    print("Decorator Working for me! I'm 'def display()'")
display()

@decorator_class 
def person(name, age):
    print(f"Function 'person' working with param/args: ({name}, {age})")
person('Cesar', 21) #caller with 2 args