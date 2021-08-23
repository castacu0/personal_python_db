import json
#>>> Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse
#   it by using the json.loads() method.

# Any Python object, can be converted it into a JSON string
#   by using the json.dumps() method.

"""
When you convert from Python to JSON,
Python objects are converted into the JSON
(JavaScript) equivalent:

Python    	JSON
dict	      Object
list      	Array
tuple     	Array
str	        String
int	        Number
float	      Number
True        true
False	      false
None	      null

"""


print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))
#                 1   2              3                     4
#4 sort the result alphabetically by keys:
