"""
Operator Overloading

The __init__() function gets called every time we create a new object of that class.
We can define a __str__() method in our class that controls how the object gets printed.
"""

"""
   For example, the + operator will perform
   arithmetic addition on two numbers, 
   merge two lists, or concatenate two strings.
   
   This feature in Python that allows the same
   operator to have different meaning according
   to the context is called operator overloading.
"""

class Point:
    def __init__(self, x0 = 0, y0 = 0):
        self.x = x0
        self.y = y0

    def __str__(self): #__str__ controls how the object gets printed
        return f"({self.x},{self.y})"

poi_1 = Point(1, 2) #caller
poi_2 = Point(89, 38) #caller

print(poi_1)
print(str(poi_1))
print(format(poi_1))
#With these 3, Python calls the    poi_1.__str__() method


print("\n\n")


"""
Overloading the + Operator

To overload the + operator, we will need to implement __add__()
"""

class Point:
    def __init__(self, x1=0, y1=0):
        self.x = x1 #7
        self.y = y1 #4

    def __str__(self):
        return f"PRINTER -- ({self.x},{self.y})"

    def __add__(self, other): #other is p2
        final_x = self.x + other.x 
        final_y = self.y + other.y
        return Point(final_x, final_y)

    def __mod__(self, otherself):
        final_x_2 = self.x % otherself.x #other.x is 5
        final_y_2 = self.y % otherself.y #other.x is 3
        return Point(final_x_2, final_y_2)

p1 = Point(7, 4)
p2 = Point(5, 3)

print(f"{p1 + p2} using __add__") #MAIN CALLER for add +
print(f"{p1 % p2} using __mod__") #MAIN CALLER for mod %



#When I use print(p1 + p2), Python calls p1.__add__(p2)
#which in turn is Point.__add__(p1,p2). 
#             class☝  method☝  ☝ ☝these two