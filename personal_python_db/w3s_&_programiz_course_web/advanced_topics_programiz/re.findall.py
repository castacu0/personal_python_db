import re

#re.findall(pattern_you_want, string)
#Example 1
string = "The rain in Spain"
x = re.findall("ai", string)
print(x) #['ai', 'ai']

#Example 2
stringX = 'hello 12 hi 893. 19865 Howdy 3874'
y = re.findall("\d+", stringX) 
print(y) #>>>['12', '893', '19865', '3874']

# re.split(pattern_you_want, string, optional maxsplit param)

# re.sub(pattern, replace, string)
    # I can pass count as a fourth parameter to the re.sub() method.

# re.subn()