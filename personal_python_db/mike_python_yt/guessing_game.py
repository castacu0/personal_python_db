secret_word = "Giraffe"
secret_word = secret_word.upper()
guess = ""
guess_count = 0

while guess != secret_word: #mientras no le atines, corre el while.
    if guess_count <= 4: #it starts in 0
        guess = input("Enter guess: ")
        guess = guess.upper()
        guess_count += 1
        if guess == secret_word: #pero si en una de esas le atinas, aqui se acaba.
            print("You win!")
            break
    else: #if guess_count is 5, stop everything
        print("Out of Guesses, YOU LOSE!")
        break