# First split
data = "Luffy is going to Onigashima"
print(data.split(" ")) #Returns a list of the words in the string

# Recommended way of spliting
dataX = "Luffy is coming from Punk Hazard"
d = " "
print(dataX.split(d)) #Returns a list of the words in the string



# --------------------------------



# Second join
j_data = ['Luffy', 'is', 'going', 'to', 'Onigashima']
print(" / ".join(j_data))  # Concatenate any number of strings.

# Recommended way of joining
j_dataX = ['Luffy', 'is', 'coming', 'from', 'Punk', 'Hazard']
d = "..."
print(d.join(j_dataX))



# IN CASE WE HAVE MIXED DATA. THESE METHODS DON'T WORK ☝
# .join() + list comprehension LIKE syntax but with parenthesis
# called GENERATOR EXPRESSION
# Remember that .join()  returns a string by joining all the elements of an ITERABLE 
# Native data types - List, Tuple, String, Dictionary, and Set.
# Numbers are not iterables

mixed_data = ["Volescu", "Murderbot", "Overse", "Ratthi", 5, 489]
to_print = " ".join(str(i)  for i in mixed_data)
                  #(this is the entire iterable)
print(to_print)

# Extra
o = '.-.-.-'.join(['Nami', 'Usopp', 'Zoro'])
print(o)


economic_growth ={"India": 7.0, "Cambodia": 7, "Tanzania": 6.9, "Bangladesh": 6.6, "Senegal": 6.6}
#it returns the keys  
str = ",".join(economic_growth)
print(str)


