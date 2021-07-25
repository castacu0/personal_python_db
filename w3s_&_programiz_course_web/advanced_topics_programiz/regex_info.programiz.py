
Metacharacters are characters that are interpreted in 
a special way by a RegEx engine. Here is a list of metacharacters:

[]  .  ^  $  *  +  ?  {}  ()  \  |

"""
[] - Square brackets

Brackets allow us to specify that're looking for characters
in a given group or that we wish to match with what is inside.
    
        Here, [abc] will match if the string you are trying to
        match contains any of the a, b or c.
        
        - [a-e] is the same as [abcde].

        - [1-4] is the same as [1234].

        - [0-39] is the same as [01239].

        You can invert the character set by using caret ^ symbol
        at the start of a square-bracket.

        - [^abc] means any character except a or b or c.

        - [^0-9] means any non-digit character.
"""
# 🔴  🔴  🔴


"""
* - Star

The star symbol * matches zero or more occurrences of the pattern 👈left to it.

txt = "The rainnnn in Spain falls maimly in the plain!"
      #Check if the string contains "ai" followed by 0 or more "n" characters:
x = re.findall("ain*", txt)

>>> ['ainn', 'ain', 'ai', 'ain']
>>> Yes, there is at least one match!

"""