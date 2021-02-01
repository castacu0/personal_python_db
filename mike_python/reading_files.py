characters1 = open("external.txt", "r")

# print(characters1.readable()) #True or False

# print(characters1.read()) #The whole thing

# print(characters1.readline()) # 1 line at the time

# print(characters1.readlines()) # Several lines. It needs more params

# print(characters1.readlines()[2]) # Several lines. It needs more params


for i in characters1.readlines():
    print(i)

characters1.close()