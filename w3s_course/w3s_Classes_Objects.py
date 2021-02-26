class Person:
  """Create a class named Person, use the __init__()
  function to assign values for name and age:
  """
  def __init__(self, nameX, ageX):
      self.name = nameX
      self.age = ageX

  def message(self):
      print(f"Hi, my name is: {self.name} and I'm {self.age}.")

if __name__ == "__main__":
    given = input("Give me a name: " )
    object1 = Person(given.capitalize(), 36)
    object1.message() 

    """
    object1.age = 45   #this helps to modify the value afterwards
    del object1.age   #it deletes de property or instance called age
    del object1   #it deletes the object
    """    