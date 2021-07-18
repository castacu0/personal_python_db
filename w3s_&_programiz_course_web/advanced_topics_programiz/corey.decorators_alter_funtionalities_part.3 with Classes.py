# PART 3
# Now we are using a Class to replicate our def decorator_func

def decorator_function(func_to_alter):
    def wrapper_function():
        print(f"Wrapper running b4 func_to_alter named '{func_to_alter.__name__}'")
        return func_to_alter() 
    return wrapper_function

@decorator_function
def display(): 
    print("Decorator Working for me! I'm DISPLAY")
display()
