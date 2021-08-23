import random
import string

def create_password(): 
    """
    It returns one or several passwords
    based on the numbers the user inputs
    when asked to do so
    """
    charactersX = string.ascii_uppercase + string.ascii_lowercase \
         + string.digits + string.punctuation

    password_saved_afterForLoop = []
    
    length = int(input("How many numbers do you want on it? "))

    for i in range(length):
        aleatory_character = random.choice(charactersX)
        password_saved_afterForLoop.append(aleatory_character)
    
    #Out of the FOR loop
    password_saved_afterForLoop = "".join(password_saved_afterForLoop) #convert it into string
    return password_saved_afterForLoop 


def run():
    password = create_password()
    print("Your new password is: ", password)


if __name__ == "__main__":
    run()