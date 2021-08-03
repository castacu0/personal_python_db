"""

>>> RegEx is like Ctrl+F

They are powerful tools to find patters in texts

It helps for scrapping, user input, etc.


Ctrl + F
Alt + R

\d = I'm searching for all valid digits from 0-9
\D = It's the opposite. Non digits

import re

This is a RegEx syntax example (mail)👇

"[a-z A-Z 0-9]+@[a-z A-Z]+\.(com|edu|net)"

[]  brackets allow us to specify that're looking for characters
    in a given group or that we wish to match with what is inside.
    (until we encounter an @ symbol, in this case) 
        #cuz we're checking for an email address
 
+   the plus sign after the brackets means we're looking for any
    combinations of one or more of these characters 
        #the second part of the mail, after the @

.  the dot is for the domain


Uppercase letters [A-Z]
Lowercase letters [a-z]
Numbers [0-9]
#a to z   A to Z   0 to 9
the + sign means more instances or objects of the same character

"""
import re
pattern = "[a-z A-Z 0-9]+@[a-z A-Z]+.(com|edu|net)"
user_input = input()
if(re.search(pattern, user_input)):
    print(f'yes')
else:
    print(f'no')
    