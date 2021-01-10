def run():
    #these variables were created OUTSIDE of the function 'calculate_ages'.
    name_1 = input("\nWhat is your name? ")
    name_2 = input("And you, my friend, what is your name? ")
    age_1 = input(f"\n{name_1}, please, tell me your age: ")
    age_2 = input(f"And now you, {name_2}, how old are you?: ")

    age1_int = int(age_1)
    age2_int = int(age_2)

    print(calculate_ages(name_1, name_2, age1_int, age2_int))


def calculate_ages(name_1, name_2, age1_int, age2_int):
    if age1_int > age2_int:
        return (f"{name_1}({age1_int}) is olden than {name_2}, who is {age2_int}")
    elif age1_int < age2_int:
        return (f"{name_1}, you're younger than {name_2}, who is {age1_int}")
    else:
        return (f"{name_1} and {name_2}. You are the same age. {age1_int}.")


if __name__ == "__main__":
    run()