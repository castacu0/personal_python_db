# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        # if ☝ not raised then run this following line 👇
        self._temperature = value # 200 for instance
        


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter


#🍁 These 2 are basically the same
print(human._temperature)
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
print(human.set_temperature(-200), "... nothing being returned") #if 300 = raised error   if 200 it runs and = -328

# Get the to_fahreheit method
print(human.to_fahrenheit()) # -328.0