"""__str__() and __repr__() functions"""


class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

pe = Person('Cesar', 57)

print(pe.__str__())  #<__main__.Person object at 0x10ff22470>
print(pe.__repr__()) #<__main__.Person object at 0x10ff22470>
#-----------------------------------------------------------------

# The default implementation is useless.
# Let’s go ahead and implement both of these methods.

class Person:

    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Person name is {self.name}, age is {self.age}. 🌀'


p = Person('Marco', 39)

#print(p) automatically prints whatever is in def __str__(self):
#but if I comment# the __str__ method. Then __repr__ enters and helps.

print(p.__str__()) #Person name is Marco and age is 39
print(p.__repr__()) #Person name is Marco, age is 39 🌀 repr 

#more info https://www.journaldev.com/22460/python-str-repr-functions
