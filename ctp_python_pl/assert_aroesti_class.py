epic_list = [12, "Second", True, "Eleven", "Hullo", 856, "",]
#            X      ✔       X       ✔         ✔    X    X

def function(epic_list):
    keeper = [] #it saves 'n',  'e',  'o'

    for each_word in epic_list:
        if type(each_word) == bool: #Instead of type = isinstance
            print(f"I don't accept {each_word} in my list")
        else:    
            try:
                assert type(each_word) == str, f"{each_word} is not a str"
                assert len(each_word) > 0, f"I do not want empty strings"
                keeper.append(each_word[4]) # based on INDEX 
            except AssertionError as err:
                print(err)
    return keeper
print("\nI accept these:", function(epic_list)) #general caller
