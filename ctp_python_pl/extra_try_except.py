try:
    filee = open(my_file)

except NameError as err: 
    print("name is not defined")
    
    # with filee:
    #     print(filee.read()) 