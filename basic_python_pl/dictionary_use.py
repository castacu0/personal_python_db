# Try 1       Doublicated Not Allowed  -  The 2nd one wins.
  # thisdict = {
  #   "brand": "Ford",
  #   "model": "Mustang",
  #   "year": 1964,
  #   "year": 2020
  # }

  # print(thisdict)

# Try 2       Dictionary Length
  # print(len(thisDictionary))

# Try 3       Any Data Type String, Boolean, Integer, List
  # thisDictionary = {
  #   "name": "Cesar",
  #   "age": 20,
  #   "male": True,
  #   "favoriteColors": ["red", "orange", "white"]
  # } 
  # print(thisDictionary["favoriteColors"][2]) #This is a List
  # #The print shows--->    white

# Try 4       Type of a Dictionary      <class 'dict'>
thisDictionary = {
  "name": "Cesar",
  "age": 20,
  "male": True
}
print(type(thisDictionary))

newdict = {i = i*i*i*i for i in thisDictionary }