# # 👑
# numbers = {"a":1, "b":2, "c":3, "d":4, "e":5}

# new1 = {key : 4 * secTrav for key,secTrav in numbers.items()}
# new2 = {key : 4 * key for key in numbers.keys()}

# print(new1)
# print(new2)

# 🎭 Looping Dictionaries 

car =   {"brand": "Ford", "model": "Mustang", "year": 1964}

for i in car:
    print(i)

print("\n")

for i in car:
    print(car[i])

print("\n")

for i in car.values():
  print(i)

print("\n")

for i in car.keys():
  print(i)

print("\n")

for key1, value2 in car.items():
  print(key1, value2)