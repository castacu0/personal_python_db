def main():
    my_list = [False, "Random", 5.8, 3]
    my_dicts = {"firstname":"Robert", "lastname":"Acuna",}

    super_list = [
        {"firstname":"Robert", "lastname":"Acuna"},
        {"firstname":"Juan", "lastname":"Mendez"},
        {"firstname":"Lupe", "lastname":"Yao"},
        {"firstname":"Marco", "lastname":"Lole"},
    ] #This is a list of Dicts
 
    super_dict = {
        "natural_n" : [1, 2, 3, 4, 5],
        "integer_n" : [-1, -2, 3, 4, -5],
        "float_n" : [1.3, 2.9, 3.6, 4.8, 5.2],
    } #This is a dict of Lists

    for key1, value2 in super_dict.items():
        print(f" --> {key1} : {value2}\n")

#BOTH WORK
    for i in super_list:
        print(i["firstname"] , "-" , i["lastname"])  #"I was missing the commas"
    
    print("\n")
    for i in super_list:
        for key, values in i.items():
            print(key,": ", values);

if __name__ == '__main__':
    main() #the caller / entry point