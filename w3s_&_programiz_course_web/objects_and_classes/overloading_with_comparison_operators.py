"""2-D coordinate system"""

# Suppose we wanted to implement the less 
# than symbol < symbol in our Point class.
from os import O_NDELAY


class Point:
    def __init__(self, x1 = 0, y1 = 0):
        self.x = x1 #1
        self.y = y1 #9

    def __str__(self):
        return f"PRINTER method {self.x}, {self.y} "

    def __lt__(self, other_object): #p1.__lt__(p2)
        self_value = self.x  + self.y
        #self_value = (self.x ** 2) + (self.y ** 2)
                      # 1*1 = 1    +    9*9 = 81    🍏Total: 82
        other_value = other_object.x + other_object.y
        #other_value = (other_object.x ** 2) + (other_object.y ** 2)
                      # -5*-5 = 25     +     8*8 = 64    🍏Total: 89
        return self_value < other_value
                #     82  <  89
    def __eq__(self, other_guy):
        one = self.x and self.y
        two = other_guy.x and other_guy.y
        return one == two

obj_1 = Point(1, 9)
obj_2 = Point(-5, -8)

ne1 = Point(4,7)
ne2 = Point(4,7)

print(f"A-. {obj_1 < obj_2}") #Is 82 less than 89?  >>> True
print(f"B-. {obj_2 < obj_1}") #Is 89 less than 82?  >>> False

print(f"__eq__ {ne1 == ne2}") #is 5,8 exactly the same as 5,8 >>>True
print(Point())