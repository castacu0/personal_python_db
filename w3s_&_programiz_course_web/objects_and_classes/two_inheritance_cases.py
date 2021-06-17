#Inheritance case 1: USING SUPER📘 

class Bird: # parent class
    
    def __init__(self):
        print("\nBird is ready...")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster BIRD")

class Penguin(Bird): # child class

    def __init__(self):
        super().__init__() #-----------------------------------  # call super() function
        print("🔥 -- Penguin is ready. Hell yeah! ")

    def whoisThis(self):
        print("🐧 -- Penguin ")

    def run(self):
        print("💨 -- Runnnn fasterrrrrrrr Penguin \n")

kamui = Penguin() #object saving the class.

kamui.whoisThis()
kamui.swim() #This comes from Bird, the father
kamui.run() #This one is new. We extended its abilities


# Bird is ready
# 🔥 -- Penguin is ready. Hell yeah!
# 🐧 -- Penguin
# Swim faster
# 💨 -- Runnnn fasterrrrrrrr



#Inheritance case 2: Importing from another file 📙 