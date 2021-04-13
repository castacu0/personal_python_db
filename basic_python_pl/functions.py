# def print_message():
#     print("Hello, buddy")
#     print("I'm learning how to use functions")

# print_message()
# print_message()
# print_message()

def entire_conversation(changing_message):
    print("Hi,friend")
    print("How are you?")
    print(changing_message) #This is the thing I wanna change
    print("See you later.")

selected_option = int(input("Select one number (1, 2, 3): "))

if selected_option == 1:
    entire_conversation("You chose number 1")

elif selected_option == 2:
    entire_conversation("You chose number 2")

elif selected_option == 3:
    entire_conversation("You chose number 3")

else:
    print("I told you to choose one of the three numbers.")