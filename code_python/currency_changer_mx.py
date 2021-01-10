nationality = input("Are you a Mexican? (Answer YES or NOT): ")

if nationality == "YES" or "yes":
    print("I'll transform your currency into USD")
    mexpesos = input("Let me know how many pesos you have: ")
    #and that information turn it into a floating number.
    mexpesos = float(mexpesos)
    currentDollar_value = 19.88
    dollars = mexpesos / currentDollar_value
    dollars = round(dollars, 2)
    dollars = str(dollars)
    print("You have $" + dollars + " dollars, congrats!")
else:
    print("I will soon add more nationalities.")
    print("Thanks for participating.")

