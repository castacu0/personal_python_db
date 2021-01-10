

def le_message(message):
    print("I'll translate 'Hello, my friend' in other language.")
    print(message) #This is the thing I wanna change
    print("I hope you liked it.")

language = str(input("Select between: es, fr, or it: "))

if language == "es": #Spanish
    le_message("Hola, amigo.")

elif language == "fr": #French
    le_message("Bonjour, mon ami.")

elif language == "it": #Italian
    le_message("Ciao, amico.")

else:
    print("I'm sorry, I just have es, fr, and it")