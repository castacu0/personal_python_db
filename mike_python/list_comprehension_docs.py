colors = ["Red","Black","Yellow","White","Blue", "Rojo"]

new0 = [traveler for traveler in colors  if "o" in traveler]
new1 = [traveler.upper() for traveler in colors  if traveler != 'Yellow']
new2 = [traveler for traveler in colors  if traveler != 'Yellow']
new3 = [traveler for traveler in colors  if traveler == 'Yellow']
#        ⬆                                                  |
#        ⬆---------------------------------------------------
newlist1 = [x if x != "Black" else "orange" for x in colors]
newlist2 = [x if x == "Black" else "orange" for x in colors]

#['Red', 'orange', 'Yellow', 'White', 'Blue', 'Rojo']
#['orange', 'Black', 'orange', 'orange', 'orange', 'orange']

print(new0)
print(new1)
print(new2)
print(new3)
print("\n\n --")
print(newlist1)
print(newlist2)

#more info here https://www.w3schools.com/python/python_lists_comprehension.asp