# using property class

"""
Any code that retrieves(regresa) the value of temperature or _temperature will automatically call get_temperature()

any code that assigns a value to temperature will automatically call set_temperature()

We can even see that set_temperature() was called (cuz its param) even when we created an object.

>>> human = Celsius(37)
Setting value...
"""
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature   # ⭐The temperature attribute is a property object which provides an interface to this private variable.

    def to_fahrenheit(self):
        print("Fah, Pasele a get_tempe ---")
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...👇")
        return self._temperature   #⭐The actual temperature value is stored in the private _temperature variable.
# Any code that retrieves(que regresa) the value of temperature or _temperature will automatically call get_temperature()

    # setter
    def set_temperature(self, valueX):
        print("Setting value...") #2nd
        if valueX < -273.15:
            raise ValueError("Temperature below -273.15 is not possible\n\n")
        self._temperature = valueX

    # creating a property object
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)    #you are calling Setting value because it has 1 parm
print("\n")
print(human.temperature, "\n") #37  #line 4
        # another line like the previous just in case >>> print(human.get_temperature()) #37  
print(human.to_fahrenheit()) #98   #lines 11,12, and 13
#human.temperature = -300