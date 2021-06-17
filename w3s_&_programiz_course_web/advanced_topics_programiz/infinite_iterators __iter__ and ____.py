#We must be careful when handling such iterators.

"""
The built-in function iter() can be called with two arguments.
  / The first parameter must be a callable object (function)
  / The second is the sentinel. 
The iterator calls this function(1st) until the returned value is equal to the sentinel (maxnum).
"""

print(int()) #int is always 0

infinite = iter(int, 1) #the sentinel never gets called
print(next(infinite))
print(next(infinite))

class Infinite_Iter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a = iter(Infinite_Iter())
print(next(a))