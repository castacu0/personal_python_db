import time

numUser = int(input("Escoge un numero: "))
operational_time = time.time()
i = 0 
#print(f"General speed {operational_time}\n")

while i**2 < numUser: 
    print(f"{i}")
    i += 1

if i**2 == numUser:
    print(f"The squared root of {numUser} is {i}.")
else:
    print(f"\nHey, {numUser} has no perfect square root.")
    print(f"However {numUser} is close to {i}.")
    print(f"---> Only 1,4,9,16,25,36,49,64,81,100 have.")
    
answer = round(time.time() - operational_time, 6) 
# 4 decimals. You can change it.

print(f"\n⌚ --> It took me: {answer} seconds to finish this.")

