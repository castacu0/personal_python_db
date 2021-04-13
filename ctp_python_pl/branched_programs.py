num_1 = int(input("Give me a number: "))
num_2 = int(input("Give me another number: "))

if num_1 > num_2:
    print(f"\nThe number {num_1} is bigger than {num_2}.")

elif num_1 < num_2:
    print(f"\nThe number {num_1} is smaller than {num_2}.")

else: #they're the same num
    print(f"\nThe number {num_1} is EQUAL to {num_2}.")