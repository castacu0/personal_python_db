# 🎈ARBITRARY ARGUMENT🎈 Using Tuples and Indexes

# def party(*kids):
#     print("The youngest child is " + kids[3])

# party("Juan","Marco", "Fili", "Margarita", "Aragorn") 
# # >>> The youngest child is Margarita.




# # keys = "values",
# def cars(three, one, two,): #parameters in def
#     #There is no order in those parameters, man!
#     print(f"I love {one}")
#     print(f"I love {three}")

# #Arguments in CALLER
# cars(one="Ferrari", two="Audi", three="Mercedes")



# def kid(firstName, lastName, age):
#     #print(f"Hi, {firstName} {lastName}. Age: {age}")
#     if firstName == "Juan":
#         return firstName

# print(kid("Juan","Acuna",9))
# # >>> Juan



# 🎈 ARBITRARY KEYWORD ARGUMENTS 🎈

# def kid(**idkHowManyParameters):
#     print("Marco, you are: " + idkHowManyParameters["one"] + " year old.")
#     #print(f"Marco, you are: {idkHowManyParameters[]} year old.")

# kid(three="3", two="2", four="4", one="1") #THE CALLER
#   #many arguments
#   # but only 1 **parameter


# # 🎈 DEFAULT PARAMETER VALUE
# def function(name="HEY, GIVE ME A VALUE klero"):
#     print("I'm from " + name)

# function("Mexico") #Caller with 1 name to replace
# function("Canada")
# function("the US")
# function()

# #Passing a list as an argument
# def something(parameter_food):
#     for eachIngredient in parameter_food:
#         print(eachIngredient)

# shopping_list = ["Eggs","Milk","Mayo","Cereal"]

# something(shopping_list)


