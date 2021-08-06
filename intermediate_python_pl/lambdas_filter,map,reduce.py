# Map, filter, and reduce take 2 parameters
from functools import reduce

my_list = [1, 7452, 8, 3, 69, 65, 7]

mapX = list(map(lambda x: x**2, my_list))
reduceX = reduce(lambda x, y: x*y, my_list) #5,614,932,960
        # reduce doesn't need of list()

generatorX = (i**2 for i in my_list)
list_comprehensionX = [i**2 for i in my_list]

print(mapX) #[1, 55532304, 64, 9, 4761, 4225, 49]
print(generatorX) #<generator object <genexpr> at 0x000001C1CEB59430>

print(list_comprehensionX) #[1, 55532304, 64, 9, 4761, 4225, 49]
print(reduceX)
