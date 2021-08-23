names = ["meRco","LucIA","vEnuS",]
laliste = [trav.upper()   for trav in names] #0123456789

#dict
ledictio = {i : f"🎫{i.lower()}"    for i in laliste    if "A" in i}

ledictio2 = {i : f"👑 {i.lower()}"    for i in laliste    if i != "LUCIA"}

print(ledictio2)
print("\n")
print(ledictio)


nums = [trav for trav in range(10)]

nx = {f"KEY: {trav}" : trav**2 for trav in nums if trav**2 % 3 == 0}
#nx = {f"KEY: {trav}" : trav**2 for trav in nums} #if trav**2 % 4 == 0}
print(nx)


long_names = ["My house", "Casa", "Ri", "Neural Network", "E", "Kot", "Jumps"]

bla = {f"KEY:{trav}" : len(trav) for trav in long_names if len(trav) > 5}
print(bla)

