
#---------- DICTIONARY WITH GET / Mike -----------
months = {
  1 : "January",
  2 : "February",
  12 : "December",
}

num = int(input("Select a num from 1 to 12: "))
print(months.get(num, "In case I put something I don't have on the list."))


# #---------- WHILE LOOPS / Mike -----------
# increase = 1 #It starts in 1
# while increase < 11:
#     print(increase)
#     increase += 1

# print("increase got to 11 so I stopped.")