def func1(one_arg, one_func):
    def func2(another_ARG):
        return another_ARG*2 #
    value = func2(one_arg)
    return one_func(value)

one_arg = 1 #this is global and runs as a parameter of  'one_arg'

def any_function(any_arggg): #GLOBAL function but no one is calling it globally.
    return any_arggg + 5

print(f"The num is: {func1(one_arg, any_function)}") #the MAIN caller

# 'any_function'  is being the parameter and an individual function.