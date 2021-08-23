# 🦠 Example 1 🦠



# 🦠 Example 2 🦠 map()
# Applies a lambda function to EACH element of an iterable.

num0 = [1, 10, 100]
num1 = [4, 5, 6]
num2 = [46, 2, 90]

iter_object = map(lambda x: x**2, num0)
print(iter_object) #<map object at 0x7f5e8fafa550>

result = map(lambda n1, n2: n1 + n2, num1, num2)
print(list(result))

result = list(map(lambda n1, n2: n1 + n2, num1, num2))
print(result)



# 🦠 Example 3 🦠 filter()
# The filter() function filters out ONLY the
# elements for which the given function returns true:

numbers = [234, 3245, 639, 550, 654]

even_numbers =  list(filter(lambda n: n % 2 == 0, numbers))

print(f"Only the even nums remained: {even_numbers}")


