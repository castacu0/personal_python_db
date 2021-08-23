#PRACTICE 1
numbers = ["\n", 1, 81, 5, 327] #my iterable
print(dir(numbers))
# I do this to identify which __special methods__ are available to use with my iterable



#PRACTICE 2
what_is = numbers.__iter__()
print(f"\n{what_is}\n") #It's a list_iterator. Good, we can work there



#PRACTICE 3
countries = ["Malawi", "Cote d'Ivoire", "Ghana", "Benin"] #normal list

c = countries.__iter__() #this is now iterable
print(c.__next__()) 
print(c.__next__()) #now this print every object
print(c.__next__()) #inside of our list countries
print(c.__next__()) #one by one
      #I can do this OR
e = iter(numbers) #numbers = [1, 81, 5, 327] 
print(next(e)) # \n
print(next(e)) # 1
print(next(e)) # 81
print(next(e)) # 5
print(next(e)) # 327



#PRACTICE 4
names = ["\nPaul", "Usul", "MuadDib", "Atreides"]
o = iter(names)

while(True): #infinite
    try:
        traveler = next(o)
        print(traveler)
    except StopIteration:
        print(f"Break this Infinite While Loop.")
        break

   #OR JUST

for i in names:
  print(i) 



#PRACTICE 5
class Practice():
    """Class to implement an iterator using iter and next 
    to get the powers of two until a certain number"""
    print("\nClass activated.")

    def __init__(self, max_num = 0): #max_num to be set by the user 👇
        self.num = max_num
        print(f"__init__ working.")

    def __str__(self):
        return f"__str__ activated at the end."

    def __iter__(self):
        self.new_one = 0
        print(f"__iter__ activated.\n")
        return self

    def __next__(self):      
        print(f"⚡ --- Next being used ---")
        if self.new_one <= self.num:
            result = 2 ** self.new_one #2^0 = 1 
            self.new_one += 1 #✔0, ✔1, ✔2, ✔3, ❌4
            return result
        else:
            raise StopIteration 

obj = Practice(3) #👈 max_num here
i = iter(obj)
print(next(i)) #it prints 1
print(next(i)) #it prints 2
print(next(i)) #it prints 4
print(next(i)) #it prints 8 #print(next(i)) #exception Raised

print(f"\n\n")

# for i in Practice(6): 
#     print(i)
#     """Ironically, this for loop is actually an infinite while loop."""