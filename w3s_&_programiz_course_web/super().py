"""
#super() with Single Inheritance🟩

class Mammal: # Mammal(object):  is similar 
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
    
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('ARGUMENT')
    
caller = Dog()

# super().__init__('Dog')
# instead of
# Mammal.__init__(self, 'Dog')
"""

#super() with Multiple Inheritance🟩
#Every var followed by an X is a Parameter
class Animal:
  def __init__(self, AnimalX):
    print(AnimalX, 'is an animal. 🐞');

class Mammal(Animal):
  def __init__(self, mammalNameX):
    print(mammalNameX, 'is a warm-blooded animal.')
    super().__init__(mammalNameX)
    
class NonWingedMammal(Mammal):
  def __init__(self, NonWingedMammalX):
    print(NonWingedMammalX, "can't fly.")
    super().__init__(NonWingedMammalX)

class NonMarineMammal(Mammal):
  def __init__(self, NonMarineMammalX):
    print(NonMarineMammalX, "can't swim.")
    super().__init__(NonMarineMammalX)

class Dog(NonMarineMammal, NonWingedMammal):
  def __init__(self):
    print('Dog has 4 legs.');
    super().__init__('🔥arg')
    
caller = Dog()
print('')
bat = NonMarineMammal('🦇 - Bat')