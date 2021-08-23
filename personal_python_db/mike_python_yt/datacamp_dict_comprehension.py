dict1 = {"a":1, "b":2, "c":3, "d":4}

compr = {k:"even" if v % 2==0 else "odd" for (k,v) in dict1.items()}
print(compr)