class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides #(3)
        self.sides = [0 for i in range(no_of_sides)]
        #it initializes all the items(side) of the list to 0

    def inputSides(self):
        self.sides = [float(input("🦑 Enter value for side " + str(i+1) + " : ")) for i in range(self.n)]

    def displaySides(self):
        for i in range(self.n): #i is 0
            print("Side", i+1, "is", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)
        #super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a) * (s-b) * (s-c)) ** 0.5
        print('🐍 The area of the triangle is %0.2f' %area)
        print(f"🐍 The area of the triangle is {area}")

t = Triangle() #caller

t.inputSides()
t.displaySides()
t.findArea()