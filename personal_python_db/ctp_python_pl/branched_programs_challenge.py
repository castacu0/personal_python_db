def run():
  name_1 = (input("\nWhat's your name? "))
  name_2 = (input("What's your friend's name? "))
  age_1 = input(f"\nHow old are you, {name_1}? ")
  age_2 = input(f"And you, {name_2}. Tell us your age: ")

  age1_int = int(age_1)
  age2_int = int(age_2)

  if age_1 > age_2:
      print(f"\n{name_1}, you're {age1_int}. You are olden than {name_2}, who is {age2_int}.")

  elif age_1 < age_2:
      print(f"\n{name_1}, you're {age1_int}. So, you are younger than {name_2}, who is {age2_int}.")

  else: #they're the same num and age
      print(f"\n{name_1} and {name_2}, you are both {age_1}.")

if __name__ == "__main__":
    run()