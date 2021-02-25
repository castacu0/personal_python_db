class Coordinates:
    """We want to know he distance
    between 2 given coordinates"""
    def __init__(self, coo_x, coo_y):
        print("init running")
        self.x = coo_x
        self.y = coo_y
#these are 👆 called instances

#                             👇 This is the object2 caller now.
#                                and a new instance.
    def distance(self, second_object):
        x_keeper = (self.x - second_object.x)**2
        #          38                71
        y_keeper = (self.y - second_object.y)**2
        #           8                2
        return (x_keeper + y_keeper)**.5

if __name__ == "__main__": #main runner and caller
    object1 = Coordinates(38, 8)
#                         x1, y1
    object2 = Coordinates(71, 2)
#                         x2, y2    
    
    var = object1.distance(object2) 
    #print("{0:.2f}".format(var)) # >>> ✔ 33.54
    print(round(var,3))           # >>> ✔ 33.541

    # Original
    # print(f"{object1.distance(object2)} meters")
    # self disappears when we use the method
    # in the caller  --->  print(object1.distance(self, object2))
