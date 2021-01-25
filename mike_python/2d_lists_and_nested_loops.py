number_grid = [[1,2,3,4], [4,5,6,7], ["a", "b", "c", "d"], [0,True,False,True]]

# save = (number_grid[3][2])
# print(save)

# if save == False:
#     print("Wow, it worked")

for row in number_grid:#0,1,2,3
    #print("The columns are about to be traveled ")
    for column in row:
        print(column)
    print("-\n")    