
# PART 1
# OK, CAREFUL HERE
# THIS METHOD WOULDN'T WORK IF OUR func_to_alter took in any param/arg

def decorator_function(func_to_alter):
    def wrapper_function():
        print(f"Wrapper running b4 func_to_alter named '{func_to_alter.__name__}'")
        #return func_to_alter() #being called ()
        func_to_alter() #same shit
    return wrapper_function
     # it's waiting for its () to work properly and activate def wrapper_function():

@decorator_function
def display(): 
    print("Decorator Working for me! I'm DISPLAY")
display()

#OK, CAREFUL HERE
#THIS METHOD WOULDN'T WORK IF OUR func_to_alter took in any param/arg

"""
>>>  🔵 THIS SYNTAX IS NUM 1
# The def display(): goes 👈👆BEFORE the object calling(displayX) and the general calling
def display(): #Im the one to be altered
    print("Decorator Working for me! I'm DISPLAY")

displayX = decorator_function(display)
 #ok so the function display is being passed inside of decorator_function and saved in a obj var

displayX() #() this is the obj var that calls the wrapper_function up there


>>> 🔵 THIS SYNTAX IS NUM 2
# The def display(): goes AFTER👉👇 the @decorator_function and does the same as:
# displayX = decorator_function(display)       displayX()

@decorator_function    #👇 I'm decorating this one
def display(): #Im the one to be altered
    print("Decorator Working for me! I'm DISPLAY")
display()   # BUT STILL I have to call it, cause, it is a function at the end of the day
"""