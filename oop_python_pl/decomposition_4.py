# Class 4 - Decomposition Practice

class Car:

    def __init__(self, modelX, manufacturerX, colorX):
        self.model = modelX
        self.manufacturer = manufacturerX
        self.color = colorX

        self._current_state = 'turned off' #private
        self._motor = Motor(cylinders = 4) #private
        self._chassis = Chassis()   #private
        self._security = Airbag() #private

    def accelerate(self, type = "slowly"):
        if type == 'quickly':
            self._motor.inject_gasoline(10)
            self._motor.temperatureX(12)
        else:
            self._motor.inject_gasoline(3)
            self._motor.temperatureX(7)
        
        self._current_state = 'in_mouvement'
        #if the car accelerates, then it is in movement


    def needBreak(self, type):

        if type == "urgent":
            self._security.emergency()
        else:
            pass


class Motor:

    def __init__(self, cylindersX, typeX="gas", defaultGasLevel=80, temperatureX=0):
        self.cylinders = cylindersX
        self.type = typeX
        self.gasLevel = defaultGasLevel
        self.current_temperature = temperatureX

    def inject_gasoline(self, quantityOfGas):
        self.gasLevel = self.gasLevel - quantityOfGas

    def temperature(self, degrees):
        self.current_temperature = self.current_temperature + degrees


class Chassis: #steel, aluminium, magnesium

    def __init__(self, materialsX):
        self.materials = materialsX

    def made_of_steel(self):
        if self.aluminium == True:
            f"Such a nice and weighless car."
        else:
            f"Mehh"


class Airbag:

    def __init__(self, stateX = "good"):
        self.state = stateX

    def emergency(self):
        print("ACCIDENT DETECTED")
        self.state = "recently used"


if __name__ == "__main__":

    object1 = Car("Escape","Ford", "Red")
    object1._chassis("Steel")
    object1.accelerate("Slow")
    object1.needBreak("Urgent")