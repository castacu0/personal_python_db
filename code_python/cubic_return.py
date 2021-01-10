    
def run():
    pass

def cube(given_num):
    return given_num*given_num*given_num

value = int(input("""Any number you chose to place here.
Will be transformed into its cubic form!
Yes, it will. Give me a number: """))

print("\nVery well, your answer is-->", (cube(value)))

if __name__ == "__main__":
    run()
