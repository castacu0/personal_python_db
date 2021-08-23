#This is wrong
# for num in range(0,100,3):
#     print(num)

#This is correct
for num in range(1,100,2):
    print(f"{num}\t",end="")
    #>>>1
    #>>>3
    #>>>5
    #>>>7
    #>>>9
    #>>>11
    #>>>13