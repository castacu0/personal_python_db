def function(parameter1):
    empty = "" #1st = O    2nd = Or    3rd = Ori
    for traveler in userPhrase:
        if traveler in "AEIOUaeiou":

            if traveler.islower(): #==True
                empty = empty + "g"
            else: # ==False
                empty = empty + "G"

        else:
            empty = empty + traveler
    return empty

userPhrase = (input("Give me a phrase: "))
print(function(userPhrase))

