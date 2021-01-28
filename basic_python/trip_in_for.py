# def run():
#     name = input("What is your name (to break it down)?: ")
#     for eachLetter in name:
#         print(eachLetter.lower().replace("a","XX"))

def run():
    phrase = input("Write an epic phrase: ")
    for eachCharacter in phrase:
        print(eachCharacter.upper(), end=", ")


if __name__ == "__main__":
    run()