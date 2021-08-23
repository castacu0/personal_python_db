number = int(input("""\n🎁 I'm your personal Calculator. 🎁
\nChoose the operation you want to apply to your numbers:\n
1 = Addition (+)
2 = Subtraction (—)
3 = Multiplication (*)
4 = Division (/)

Now, choose one ---> """))

def run():
    if number == 1 or number == 2 or number == 3 or number == 4:
        num1 = int(input("Give me one number: "))
        num2 = int(input("Give me another number: "))
        message = ("\nThis is your result: ")
        if number == 1: 
            print(f"{message}{num1+num2}")
        elif number == 2: 
            print(f"{message}{num1-num2}")
        elif number == 3: 
            print(f"{message}{num1*num2}")
        else: #number == 4: 
            print(f"{message}{num1/num2}")
    else:
        print("\nGet out.")    

if __name__ == "__main__":
    run()
