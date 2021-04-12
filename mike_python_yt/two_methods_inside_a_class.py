from LaptopX import Laptop

first_laptop = Laptop("Grey", True, 2020) #Windows
second_laptop = Laptop("White", False, 2007) #Mac
               #👆 object and its 3 arguments

print(first_laptop.it_is_windows()) #>>> True
print("\n ---")
print(second_laptop.it_is_windows()) #>>> False

