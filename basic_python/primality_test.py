 
def isPrime(number): 
    contador = 0

    if number <= 1:
        return False


    for i in range(1, number + 1):
        if i == 1 or i == number:
            #if the iteration is 1 or the number, ignore it
            continue
        if number % i == 0:
            contador += 1
            #if there are modules = 0, give them a point
            break


    if contador == 0:
        return True
    else:
        return False


def run():
    number = int(input("Write a number: "))

    if isPrime(number): # == True: can be omitted
        print(str(number) + " is a Prime Number")
    else:
        print(str(number) + " is NOT a Prime Number")


if __name__ == "__main__":
    run() 