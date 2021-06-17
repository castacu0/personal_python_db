#Encapsulation 🍎
#Private variables _ or __


class Computer:

    def __init__(self):
        self.__maxprice = 800 #private variable

    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, priceX): #Careful with "setMaxPrice()"
        self.__maxprice = priceX

c = Computer()
c.sell()

# trying to change the price
c.__maxprice = 9977
c.sell() #DIDN'T WORK cause it's private

# using in-built setter function
c.setMaxPrice(1000) #This is PriceX
c.sell()

print("\n")
"""
Selling Price: 800
Selling Price: 800 
Selling Price: 1000
"""
