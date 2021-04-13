#print(f"Hello\nWorld!") 

# A hiden '\n' is at the end of every 'print'
# By typing   end=", "   you are changing that rule.

for iterator in range(0,15):
    if iterator < 14:
        print(iterator, end=", ")
    else:
        print(iterator)