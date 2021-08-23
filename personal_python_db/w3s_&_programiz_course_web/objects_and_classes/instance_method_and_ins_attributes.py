class Parrot:
    
    # instance attributes
    def __init__(self, nameX, ageX):
        self.name = nameX
        self.age = ageX
    
    # instance methods
    def sing(self, song):
        return f"{self.name} sings {song}"
    def dance(self):
        return f"{self.name} is now dancing"


# iniciate and instantiate the instace object: blu
blu = Parrot("Blu", 10)

# printer and CALLER of our instance object(blu) with is instance methods(sing or dance)
print(blu.sing("'When I am gone'"))
print(blu.dance())