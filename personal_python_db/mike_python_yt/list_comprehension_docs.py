colors = ["Red","Black","Yellow","White","Blue", "Rojo"]

new0 = [traveler for traveler in colors  if "o" in traveler]
new1 = [traveler.upper() for traveler in colors  if traveler != 'Yellow']
new2 = [traveler for traveler in colors  if traveler != 'Yellow']
new3 = [traveler for traveler in colors  if traveler == 'Yellow']
#        ⬆                                                  |
#        ⬆---------------------------------------------------
newlist1 = [x if x != "Black" else "orange" for x in colors]
"Return the item if it is not Black, if it is Black return orange".
#['Red', 'orange', 'Yellow', 'White', 'Blue', 'Rojo']

newlist2 = [x if x == "Black" else "orange" for x in colors]
"Return the item if it IS 'Black?, but if it's something else then return orange".

#['orange', 'Black', 'orange', 'orange', 'orange', 'orange']



""" 
The expression can also contain conditions, not like a filter,
    but as a way to manipulate the outcome:

>>> newlist = [x if x != "banana" else "orange" for x in fruits]

The expression in the example above says:
"Return the item if it is not banana, if it is banana return orange".
"""
print(new0)
print(new1)
print(new2)
print(new3)
print("\n\n --")
print(newlist1)
print(newlist2)
print("\n\n --")

#more info here https://www.w3schools.com/python/python_lists_comprehension.asp