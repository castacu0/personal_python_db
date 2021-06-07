#Class objects support two kinds of operations: attribute references and instantiation.

#attribute reference
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return "This doesn't return anything. It's just an example" 

print(MyClass.i)
print(MyClass.f)

# Instantiation is saving a class inside
# of a variable, and then callint the
# variable to work with it

#Like with:  ----->   blu= Parrot("", 10)