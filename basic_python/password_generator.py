import random
import string

def create_password(): #The Process starts
    # 4 lists of symbols to combine.
    mayus =list(string.ascii_uppercase)
    #mayus = ['A', 'B' , 'C', 'D', 'E', 'F' , 'G' , 'H', 'I', 'J', 'K', 'L' , 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = list(string.ascii_lowercase)
    #lower_case = ['a', 'b' , 'c', 'd', 'e', 'f' , 'g' , 'h', 'i', 'j', 'k', 'l' , 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = list(string.digits) #numbers

    symbols = list(string.punctuation)

    combinating_everything = mayus + lower + symbols + numbers

    password_saved_afterForLoop = []
    length = int(input("How many numbers do you want on it? "))

    for i in range(length):
        aleatory_character = random.choice(combinating_everything)
        password_saved_afterForLoop.append(aleatory_character)
    
    #Out of the FOR loop
    password_saved_afterForLoop = "".join(password_saved_afterForLoop) #convert it into string
    return password_saved_afterForLoop 


def run():
    password = create_password()
    print("Your new password is: ", password)


if __name__ == "__main__":
    run()