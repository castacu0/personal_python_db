numUser = int(input(f"Give me a num: "))
almostZero = 0.1
numGuesses = 0
i = 0.0
jump = almostZero**2

while abs(i**2 - numUser) >= almostZero and i <= numUser:
    i += jump
    numGuesses += 1
    print(f"numGuesses = {numGuesses}")

if abs(i**2 - numUser) >= almostZero:
        print(f"\nFailed on square root of {numUser}")
else:
        print(f"\n{i}, is close to the sr of: {numUser}") 