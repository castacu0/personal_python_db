# def getFactorialOf(aNumber):
#     if aNumber < 2: #NO aNumber > 2
#         return 1  #so it is 0 or 1.
#         #Return 1 because that's their factorial

#     else: #I chose 5✅ #otherwise
#         return aNumber * getFactorialOf(aNumber-1)
#         # 5 * getFactorialOf(4)
#         # 5 * 4 * 3 * 2 * 1  =  120
#         # print(result) #print this loop several times until we get to 5

# print(getFactorialOf(5))
# # aNumber is a parameter
# # 5 is its argument

def getFactorialOf(aNumber): #5
    if aNumber > 1: #✅ #osea 2, or 3, or 4, 5, 6 and so on
        #return aNumber * getFactorialOf(aNumber - 1)
        loops = aNumber * getFactorialOf(aNumber - 1)
        print(loops)
        return loops
    else: #if aNumber < 2: 
        return 1 #so it is 0 or 1.

#print(getFactorialOf(5))
getFactorialOf(5)