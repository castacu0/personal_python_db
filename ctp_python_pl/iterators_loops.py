external_counter = 0
internal_counter = 0

while external_counter < 4:
    while internal_counter < 3:
        print(f"Ext: {external_counter}, Int: {internal_counter}") #both 'while' loops
        internal_counter +=1
        if internal_counter == 2:
            break  #if internal_counter gets to 2, forget that I told you to get to 3 in the while
    print("\n")
    external_counter +=1
    internal_counter = 0


# counter = 0

# while counter <= 10:
#     print(counter)
#     counter += 1 
#     # counter = counter + 1