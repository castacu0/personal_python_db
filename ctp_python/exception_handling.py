"""We create a Function which has 2 parameters 'lista' and 'divisor'.
Their values(future arguments of our parameter) are already set as
global values"""
def divide_elements_in_a_list(lista, divisor):
    
    """The program will try to make the operation"""
    try:
        return [i / divisor for i in lista]
    #"""In case of error of type 'ZeroDivisorError, which means we
    # are dividing between zero, the program will execute this except
    # Or this next instruction"""
    except ZeroDivisionError as error:
        """This print helps me understand what is inside of e: or error: """
        print(f"You have an error: {error}")
        return lista
        # the 'lista' list will be printed ---> 0123456789
        #Instead of stopping the whole program.

lista = list(range(10))
divisor = 2

print(divide_elements_in_a_list(lista, divisor))