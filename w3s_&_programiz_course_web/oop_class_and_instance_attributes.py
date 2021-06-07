class Parrot:

    # class attribute or class variable
    species = "bird"

    # instance attribute 
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

"""attribute references"""
# access the class attributes
print(f"Blu is a nice {Parrot.species}") 
#It worked.👆 1st I called the class then the CLASS ATTRIBUTE not the instance one  
print(f"Woo is also a {Parrot.species}")


"""instantiation"""
# access the instance attributes
print(f"\n{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.name} years old")