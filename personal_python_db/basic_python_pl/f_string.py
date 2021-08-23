# Try 1       f-strings  { } Multiplication
  # print(f"{2 * 88}")

# Try 2       f-strings  { }
  # course = "PreWork"
  # platform = "Platzi"

  # print(f"The newest {platform}'s course is named {course}. ")

# Try 3       f-strings  { }
  # course = "PreWork"
  # platform = "Platzi"

  # print(
  #     f"The new {course} course is "
  #     f"available in {platform}."
  # )

# Try 4       %-formatting
  # name = "Cesar"
  # lastName = "Acuna"
  # age = 22


  # print("Hello, %s %s, you're %s,") % (name, lastName, age)

# Try 5       str.format()
  # name = "Cesar"
  # age = 24

  # print("Hullo, {0}. You are {1}. ".format(name, age)) 
  #   # tuples by their index

# Try 6       str.format()
  # myPerson = {"name": "Cesar", "age": 28, "body": "tall"}

  # print("Hello, {name}, you are {age}, and {body}.".format(name=myPerson["name"],
  # age=myPerson["age"], body=myPerson["body"]))

# Try 7       str.format() with **
  # myPerson = {"name": "Cesar", "age": 28, "body": "tall"}

  # print("Hello, {name}, you are {age}, and {body}.".format(**myPerson))

  # #You can also use ** to do this neat trick with dictionaries:

# Try 8       f-strings  { } with Capital F and .upper()
  # nom = "ArTuRo"
  # lage = 20
  # print(F"Salut, {nom.upper()}. Tu as {lage} ans.")

# Try 9       f-strings with Functions and methods like .lower
  # def convertToUpperCase(input):
  #       return input.upper()

  # nameX = "CeSaR CaStAnOn"

  # print(f"{convertToUpperCase(nameX)} is funny.")

  # #'eric idle is funny.')

# Try 10       f-strings calling two Methods
  # nameXE = " cESAr "
  # print(f"What's up {nameXE.strip().upper()}. We're using 2 methods")

    # .strip() is for blank spaces and .upper() helps to capitalize.

# Try 11        f-Strings    Multiline strings
  # name = "Cesar"
  # profession = "Student"
  # affiliation = "The Fire O"

  # myMessage = (
  #     f"Hello {name}. " \
  #     f"You are a {profession}. "  \
  #     f"You worked in {affiliation}."
  # )

  # print(myMessage)

# Try 12        f-Strings with 3 quotations marks """   """
  # print(f"""My name is Juan""")

# Try 13      DO NOT mix "" Equal Quotation Marks ''
  # name = "Marcos"
  # age = 90
  # print(f"The 'comedian' is {name}, aged {age}.")

# Try 14 With a Dictionary
  # dictionary = {"name": "Koko", "age": 80}
  # print(f'My name is {dictionary["name"]}, and I am {dictionary["age"]}.')

# Try 15      f-Strings    Braces
print(f"{{{70 + 4}}}")    # Result = {74} 
print(f"{{70 + 4}}")      # Result = {70 + 4}
print(f"{70 + 4}")        # Result = 74