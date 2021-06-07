from BirdX import Bird

class Penguin(Bird): # child class

    def __init__(self):
        print("🔥 -- Penguin is ready. Hell yeah! ")

    def whoisThis(self):
        print("🐧 -- Penguin ")

    def run(self):
        print("💨 -- Runnnn fasterrrrrrrr \n")

b = Bird()
b.__init__

Kamui = Penguin() #object saving the class.

Kamui.whoisThis() #MAGIC HAPPENS HERE 🚥
Kamui.swim() #This comes from Bird, the father
Kamui.run() #This one is new. We extended its abilities