class Coordinates:
    """We want to know he distance
    between 2 given coordinates"""
    def __init__(self, coo_x, coo_y):
        self.x = coo_x
        self.y = coo_y

    def distance(self, second_object):
        x_keeper = (self.x - second_object.x)**2
        y_keeper = (self.y - second_object.y)**2
        return (x_keeper + y_keeper)**.5

if __name__ == "__main__": 
    object1 = Coordinates(38, 8)
    object2 = Coordinates(71, 2)

    print(f"Meters: {object1.distance(object2)}")
    print(f"Check 1: {isinstance(object2, Coordinates)}")
    #             Please check if object2 is being passed as
    #             an instance of the Class Coordinates.
    print(f"Check 2: {isinstance(54, Coordinates)}")

