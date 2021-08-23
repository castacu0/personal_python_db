#We must be careful when handling such iterators.

"""
The built-in function iter() can be called with two arguments.
  / The first parameter must be a callable object (function)
  / The second is the sentinel. 

The iterator calls this function(1st) until the returned value is equal to the sentinel (maxnum).
"""

print(int()) #int is always 0

infinite = iter(int, 1) #the sentinel never gets called because they-re never equal
print(next(infinite)) #0
print(next(infinite)) #0
print("\n")

#----------------------------------------------------------

class Infinite_Iter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num0 = self.num
        self.num += 2
        return num0

a = iter(Infinite_Iter())
print(next(a)) #1
print(next(a)) #3
print(next(a)) #5
print(next(a)) #7
print(next(a)) #9

# 0
# 0
# 0
 
 # ---------------------
 
# 1
# 3
# 5
# 7
# 9