def operation(lista, divisor): #This is the 2nd caller
    """It returns the operation depending on the 'divisor' """
    try:
        return [trav / divisor  for trav in lista]
    
    except ZeroDivisionError: # as err:
        divisor = int(input("Second round --> "))
        return operation(lista, divisor)

def run(): #This is the 2nd caller
    lista = list(range(10))
    divisor = int(input("Give me a divisor number: "))   # divisor = 0   #or
    print(operation(lista, divisor))

if __name__ == '__main__':
    run() #This is the 1st caller