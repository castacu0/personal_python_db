#Challenge🚗

# def main():
#     warehouse = []
#     for i in range(1,11):
#         warehouse.append(i**2)
#     print(warehouse)

def main():
    """
    Save only numbers not divisible by 3

    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
     x  x  o  x   x    o   x   x   o   x

    I used 2 methods for the 'if conditional.'
    """
    warehouse = []
    for i in range(1,11):
        if i % 3 != 0: #If the division returns everything but 0. RUN the block
            warehouse.append(i**2)
        # if i**2 % 3 == 0:
        #     continue #if it is True. Skip it
        # warehouse.append(i**2)
    print(warehouse)


#LIST COMPREHENSION 🚧
# def main():
#     natural = [trav**2 for trav in range(1,11)]
#     print(natural)

if __name__ == '__main__':
    main()