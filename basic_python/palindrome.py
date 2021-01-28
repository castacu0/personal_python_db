def palindrome(word):
    word = word.replace(" ", "").lower()

    if word[::] == word[::-1]:
        return True

    else:
        return False


def run():
    word = input("Give me a word to check it: ")
    if palindrome(word):
        print("It is a Palindrome.")

    else:
        print("It is NOT a Palindrome.")

if __name__ == "__main__":
    run()