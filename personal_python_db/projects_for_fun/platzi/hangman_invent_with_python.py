import random

WORDS = 'ant bear beaver camel cat clam cobra eagle snake spider zebra'.split()

def random_word_func(wordList):
    idx = random.randint(0, len(wordList) - 1)
    return wordList[idx]


def display_board(missedLetters, correctLetters, random_word):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    hidden_word_u = '_' * len(random_word)
    for i in range(len(random_word)): 
        if random_word[i] in correctLetters:
            hidden_word_u = hidden_word_u[:i] + random_word[i] + hidden_word_u[i+1:]

    for letter in hidden_word_u: 
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
      print('Guess a letter.')
      guess = input()
      guess = guess.lower()
      if len(guess) != 1:
          print('Please enter a single letter.')
      elif guess in alreadyGuessed:
          print('You have already guessed that letter. Choose again.')
      elif guess not in 'abcdefghijklmnopqrstuvwxyz':
          print('Please enter a LETTER.')
      else:
          return guess


def playAgain():
     print('Do you want to play again? (yes or no)')
     return input().lower().startswith('y')


print("LET'S PLAY SOME HANGMAN")
missedLetters = ''
correctLetters = ''
random_word = random_word_func(WORDS)
gameIsDone = False

while True:
    display_board(missedLetters, correctLetters, random_word)

    guess = getGuess(missedLetters + correctLetters)

    if guess in random_word:
        correctLetters = correctLetters + guess
        foundAllLetters = True

        for i in range(len(random_word)):
            if random_word[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + random_word + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
             display_board(missedLetters, correctLetters, random_word)
             print('You have run out of guesses!\nAfter ' +
                 str(len(missedLetters)) + ' missed guesses and ' +
                 str(len(correctLetters)) + ' correct guesses,
                 the word was "' + random_word + '"')
             gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            random_word = random_word_func(WORDS)
        else:
            break