def whole_shit():
    epsilon = 0.01
    i = 0
    jump = epsilon**2

    selected_method = int(input("""
    I have 3 methods to divine a squared root.
        1 --> Binary Search. 🟡
        2 --> Solution Approach. 🟢
        3 --> Comprehensive Enumeration. 🔵
    Choose the method to use:  """))

    if selected_method == 1 or selected_method == 2 or selected_method == 3:
        numUser = int(input(f"""\n        Good choice. ✔
        Now, give me a number to give you its squared root: """))
        if selected_method == 1:
            print("\n--------------------------------------------")    # brute force
            print("\nBecause you chose the Binary Search. 🟡")
            print(f"Here you have your answer.\n")
            down = 0.0
            up = max(1.0, numUser)
            middle_value = (down+up)/2
                
            while abs(middle_value**2 - numUser) >= epsilon:
                print(f" down: {down}   ///   middle value: {middle_value}   ///   up: {up}\n")
                if middle_value**2 < numUser: #4
                    down = middle_value
                else:
                    up = middle_value
                middle_value = (down + up) / 2  #NEW ONE, out of the loop.
                rounded = round(middle_value, 3)
            # print(f"The square root of {numUser} is {middle_value}")
            print(f"The square root of {numUser} is {rounded}")

        elif selected_method == 2:
            print("\n--------------------------------------------")   
            print("\nBecause you chose the Solution Approach. 🟢")    
            print(f"Here you have your answer.")
            while abs(i**2 - numUser) >= epsilon and i <= numUser:
                i += jump

            if abs(i**2 - numUser) >= epsilon:
                print(f'No se encontro la raiz cuadrada de: {numUser}')
                
            else:
                answer = round(i, 2) 
                print(f'\nThe square root of {numUser} is close to: {i} ')
                print(f'However, the square root of {numUser} rounded could be: {answer} \n')

        else: #so 3
            print("\n--------------------------------------------")
            print("\nBecause you chose the Comprehensive Enumeration. 🔵") 
            print(f"Here you have your answer.\n")
            while i**2 < numUser: 
                print(f"{i}")
                i += 1
            if i**2 == numUser:
                print(f"The squared root of {numUser} is {i}\n")
            else:
                print(f"\nHey, {numUser} has no perfect square root.")
                print(f"---> Only 1,4,9,16,25,36,49,64,81,100.\n")
    else:
        print(f"\n --> I only have 3 methods. Try to play again. ❌")


def run():
    print(whole_shit)


if __name__ == "__main__":
    whole_shit()
