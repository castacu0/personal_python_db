def main(): 
    pass

def tableNumbers():
    addedNum = int(input("¿Which # do you desire to multiply?: "))
    untilWhichNum = int(input("Until which number?: "))
    myOwnRange = range(1, untilWhichNum+1)
                  # the number 1 means the 1st cake part [ : ]
    for iterator in myOwnRange:
        print(f"{addedNum} * {iterator} = {iterator * addedNum}")


if __name__ == '__main__':
    tableNumbers()