# def addition(a, b):
#     total = a + b
#     return total #to addition

# print(addition(2,3)) #and then print addition, which is a SUM with these 2 parameters

def complete_name(name, lastName, inverse=False):
    if inverse == True:  #
        return f"{lastName}{name}"
    else: #it is still False
        return f"{name}{lastName}"

print(complete_name("Cesar ", "Acuna. ", inverse=True))
print(complete_name("Cesar ", "Acuna ", inverse=False))
print(complete_name(lastName="CASTANON ", name="ARTUROOO ")) #false
