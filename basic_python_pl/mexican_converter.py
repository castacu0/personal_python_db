mexpesos = input("Hello, so, tell me, how many pesos do you have?: ")
#You put the amount in the Mexican currency
mexpesos = float(mexpesos) #This accepts decimal stuff
currentDollar_value = 21
dollars = mexpesos / currentDollar_value
dollars = round(dollars, 1)
dollars = str(dollars) #this is returning a number into a string
print("There you go, you've got $" + dollars + " american dollars right now")