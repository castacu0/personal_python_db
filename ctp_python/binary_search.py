#Chosen number 9
userNum = int(input("Give me a number: "))
epsilon = 0.01   #epsilon
down = 0.0
up = max(1.0, userNum)
middle_value = (down + up) / 2
guesses = 1

while abs(middle_value**2 - userNum) >= epsilon:
    print(f"\n1-. This is the middle value: {middle_value}")
    print(f"2-. This is the value of middle value^2, squared: {middle_value**2}")
    print(f"3-. Here is the Middle value^2 ({middle_value**2}) MINUS the user number({userNum}): ---> {abs(middle_value**2 - userNum)}")
    #print(f"3-.   REMEMBER that  'abs'  turns a negative number into a positive.☝           ⬆")
    print(f"4-. down: {down}   ///   middle value: {middle_value}   ///   up: {up}\n")
    if middle_value**2 < userNum: #4
        down = middle_value
    else: #if i^2 > userNum:
        up = middle_value

    middle_value = (down + up) / 2 #
    print(f"*** 🧧 Now the middle_value has been updated to: {middle_value}")
    print(f"BECAUSE: newest Up({up})  +  newest Down({down}) / 2 = {middle_value} 🧧")
    print(f"***  - After finishing the {guesses} loop.")
    print(f"*** 🎆 Remember UP is NOT 5 anymore. It changed with the iteration to {up}\n\n\n")

    guesses += 1

print(f'The square root of {userNum} is {middle_value}')
print(f"It took me {guesses} to discover it.")