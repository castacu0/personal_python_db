def the_convertion(equivalence, nationality):  #This is the function
    pesos = float(input("How many " + nationality + " pesos do you have?:  "))
    dollars = str(round(pesos/equivalence,2))    
    print("Woah, you have $" + dollars + " dollars.")
    print("Thanks for participating.")

usersOption = int(input("""
Welcome to this Currency Converter. 💲 🤑
My name is Atlas. 🐱‍🏍
Please, choose one of the three options: 

1-. Colombian pesos 🎆
2-. Argentine pesos 🎇
3-. Mexican pesos 🎍

Now, type the number here ➡  """))
if usersOption == 1: #Colombia
    the_convertion(3660, "Colombian")
elif usersOption == 2:
    the_convertion(70.66, "Argentine")
elif usersOption == 3:
    the_convertion(21.32, "Mexican")
else:
    print("I don't get it :( ")