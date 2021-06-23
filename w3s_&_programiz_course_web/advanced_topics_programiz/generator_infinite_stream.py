def all_even():
    "Prints all even numbers you want (in theory)."
    n = 0
    while True:
        yield n
        n += 2

r = all_even()
for i in r:
    print(i)
