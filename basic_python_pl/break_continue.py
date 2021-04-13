# 1.      With just one print
  #print(0,2,4,6,8,10)

# 2.      For loop
  # def run():
  #     for i in range(0,1000,2): #From 0 to 999 jumping every 2
  #       print(i)

# 3.      For and %
  # def run():
  #     for i in range(0,11):  #From 0 to 999 jumping every 2
  #         if i % 2 == 0:
  #             print(i)

# 4.      For 
  # def run():
  #     print([i for i in range(0,11) if i % 2 == 0])
  # # $  [0, 2, 4, 6, 8, 10]

# 5.      Continue 
def run():
  for i in range(1,100):
      if i % 2 == 0: 
           continue
      print(i)

# 6.      Break 
  # def run():
  #     for i in range(0,1000):
  #         if i == 352: #it stops at 351.
  #             break
  #         print(i)

# 7.      Travel a text  /  Checking one by one
  # def run():
  #     epicPhrase = input("Type an epic phrase: ")

  #     for givenLetter in epicPhrase:
  #         if givenLetter == "o": 
  #             break
  #         print(givenLetter)


if __name__ == "__main__":
    run()