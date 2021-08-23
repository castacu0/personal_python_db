usdollars = input("How many USdollars do you have: ")
#You put the amount in the American currency...
usdollars = float(usdollars) 
peso_value = 0.044
pesitos = usdollars / peso_value
pesitos = round(pesitos, 2)
pesitos = str(pesitos)
print("These are the pesos you have $" + pesitos + ". Enjoy yourself." )
