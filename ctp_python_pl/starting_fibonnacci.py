# 1, 1, 2, 3, 5, 8, 13, 21

def fibonnacci(num):
    if num == 1: #First digit
        return 1 #because the factorial of 1! is 1
    elif num == 2: #Second number of the secuence
        return 1 #because the factorial of 1! is 1, as well.
    elif num > 2: #so 4
        return fibonnacci(num-1) + fibonnacci(num-2) 

num = int(input("Give me a number: "))
print("9", fibonnacci(num))
