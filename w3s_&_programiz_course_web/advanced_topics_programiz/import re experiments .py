
import re

string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)
print(match) #>>> <re.Match object; span=(0, 6), match='Python'>
print(match.start()) #>>> 0

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")  

# Output: pattern found inside the string
