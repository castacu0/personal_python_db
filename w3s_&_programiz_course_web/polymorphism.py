class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot CANNOT swim")

class Penguin:

    def fly(self):
        print("Penguin CANNOT fly")
    
    def swim(self):
        print("Penguin can swim")

# FILTER: common interface. 
# A function 🟨 with 1 param 🟩
def flying_test(bird):
    bird.fly()
    #blu.fly()
    #kamui.fly()

#The callers and objects saving the classes
blu = Parrot()
kamui = Penguin()

# Calling the function 🟨 with one arg 🟥
flying_test(blu)
flying_test(kamui)