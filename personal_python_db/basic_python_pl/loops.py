def run():
    LIMIT = 100000  
    #LIMIT is the constant.

    myCounter = 0
    the2Potency = 2**myCounter   #2 at the power of myCounter {which is 0} = 1 

#Once you've understood this 
#first part, you should work on
#the 'while loop' fron now on.
    while the2Potency < limit:
        print("2 at the power of " + str(myCounter) 
        + " is equal to: " + str(the2Potency))
        myCounter +=1 
        the2Potency = 2**myCounter

# (Entry Point) - Good Practice
if __name__ == "__main__":
    run()

#2 at the power of 0 is 1
#2 at the power of 1 is 2
#2 at the power of 2 is 4