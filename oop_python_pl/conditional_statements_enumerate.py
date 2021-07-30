users = ["Test User 1", "Real User 2", "Real User 3", "John", "Mary"]

for eachNum, object in enumerate(users, start=1):
    if eachNum == 1:
        print("Extra verbose output for:", object)
    elif eachNum == 3:
        print("Num 3 running:", object)
    else:
        print(">>>", object)