def finding_maxNum(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1 #so the 1 is the biggest
        
    if num2 >= num1 and num2 >= num3:
        return num2 #so the 2 is the biggest

    else:
        return num3 #so the 3 is the biggest

print(f"The biggest of them is: {finding_maxNum(7, 4, 12)}")        #caller
# with 3 args/params
print(finding_maxNum(7,4,12))
#DON'T FORGET TO CHOOSE THE NUMBERS AS ARGUMENTS TO COMPARE