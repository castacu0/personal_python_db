# PART 2
# OK, CAREFUL HERE
# Now we are using   >>> *args and **kwargs

# We are now passing several param/args to our wrapper inside of the main decorator_function
# Also, we are decorating 2 def functions

def decorator_function(func_to_alter):
    def wrapper_function():
        print(f"Wrapper running b4 func_to_alter named '{func_to_alter.__name__}'")
        return func_to_alter() 
    return wrapper_function

@decorator_function
def display(): 
    print("Decorator Working for me! I'm DISPLAY")
display()
