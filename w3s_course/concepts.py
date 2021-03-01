#COMMENTS '''''''''''''''''''''''''''''''
#get the type
a = 0
b = "Cesar"
print(type(a))

#VARIABLES ''''''''''''''''''''''''''''''
#Variable names are case-sensitive (age, Age and AGE are 3 different variables)

#multiple variables and values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#assign the same value to multiple variables in one line
x = y = z = "Oxxo"
print(x)
print(y)
print(z)

#Unpacking
heroes = ["Frodo", "Aragorn", "Morgoth"] #list
keep_1, keep_2, keep_3 = heroes
# this is the squeezed place and we want 3 new vars
print(keep_1)
print(keep_2)
print(keep_3)

#Global variables
def myfunc():
  global h
  h = "fantastic, meh!"
myfunc() #caller

print("Python is " + h) # h was local



#DATA TYPES '''''''''''''''''''''''''''''''
# All good, I just printed physical sheets

#NUMBERS '''''''''''''''''''''''''''''''
#int, float, complex, and type conversion

#STRINGS '''''''''''''''''''''''''''''''
print("\n")

#Multiline Strings
var = """You can assign a multiline string to
a variable by using three quotes:"""
'''or with single '''

# Check Certain phrase in String or if NOT
txt = "The best things in life are free!"

if "bests" in txt:
    print("best is there")
elif "coca" in txt : 
    print("COCA is not here")
else:
  print("OUT")

# Slicing Strings
string = "I'm a string, and you?"
print(string[-7:-3]) #or [2:11:2]  

# Modifying Strings with Methods
# the .format() is quite interesting
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

#as well as
#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."
print(txt.format(13800000000))#13,800,000,000

