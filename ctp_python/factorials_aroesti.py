def recursion(userNum):
    """We get the Factorial of a given number
       
       We receive a number from the user an
       we give them the result.
       First of all. We declare our 'base case'

       Parameters:
    """
    print("In this loop my value is: ",userNum) #before starting the process print whatever shit you're doing
    if userNum > 1: # 2,3,4,5,6,7,8,9
        return userNum*recursion(userNum-1)
    else: #1 or 0                     👆 ARGUMENT!
        return 1 #why 1? because the factorial of 0 is 1 and same case for 1.
userNum = int(input("Give me a number: "))
print("\nThe factorial of", userNum, "is", recursion(userNum)) 
#the argument is what the user chose