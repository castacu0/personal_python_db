# More Generators and Yield stuff

# ⭐1st Example
def rev_str(x):
    length = len(x)
    for i in range(length - 1, -1, -1):
        yield x[i]

# For loop to reverse the string
for z in rev_str("hello"):
    print(z, end="") #olleh


# ⭐2nd Example
my_list = [9, 4, 6, 10]
          #81 16 36 100
a = (x**2 for x in my_list)                 # Generator expression
print(f"\n{a}\n") #  <genexpr> at 0x7f142
print(next(a)) # We should call them one by one or with a for loop
print(next(a))
print(next(a))
print(next(a))


# ⭐3rd Example
#Generator expressions can be used as function parameters/arguments in this case          
print(f"\n Using SUM: {sum(x**2 for x in my_list)}") # the sum of the returned ones: 233
print(f"\n Using MAX: {max(x**2 for x in my_list)}") # max num returned from the gen expression
