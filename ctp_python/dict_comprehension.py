
# WORST DOCUMENT EVER. 
# Don't even try to read it. 
# I used it to practice in the console.

exampleD = { "name": "Cesar", "age": 20, "male": True }
numbers = {"a":1, "b":2, "c":3, "d":4, "e":5}

newDictionary = {key : 4 * secTrav for key,secTrav in numbers.items()}
new2Dictionary = {key : 4 * key for key in numbers.keys()}

keys = numbers.keys()
values = numbers.values()
items = numbers.items()

if "age" in exampleD:
    print("Yes, 'age' is one of the keys in the exampleD dictionary💰\n")


exampleD["nationality"] = "Mexican" #Adding

numbers.update({"b": 87})

print(newDictionary)
print(new2Dictionary)
print("\n")
print(keys)
print(values)
print(items)
print("\n")
#print(pass)
print(exampleD)
exampleD.pop("age")
print(numbers)
numbers.popitem()
print(exampleD)
print(numbers) 
print("\n\n")
del exampleD["name"]
newD = numbers.get("f", "Not a valid key")
print(exampleD) #jelp
print(newD) #jelp
