def run():
    my_dictionary = {
      'key1': 1,
      'key2': 2,
      'key3': 3
    }

    countries_Population = {
        'Mexico': 120_034_060,
        'Paraguay': 31_598_121,
        'Argentina': 44_673_129,
    }

# 🔴 3 different ways of using 'strings' 🔴

for each_Country, population in countries_Population.items():
    print("In", each_Country, "we've:", population, "people") #1 🔴
             # with commas 👆
    print(each_Country + " has: " + str(population) + " people") #2 🔴
             # with plus signs    👆
    print(f"In {each_Country} we have {population} people") #3 🔴
             # with the f"{}" syntax 👆

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

    # Cut a long line with --> \
    print("\n" "\t" "\r" "",end=" ") #New line / tab / carriage return 
# Avoid using the f"{}" format with dictionaries
# or places were there are no indexes


    # print(my_dictionary['key1'])
    # print(my_dictionary['key2'])
    # print(my_dictionary['key3'])

    # print(countries_Population['Mexico'])

    # for each_Country in countries_Population.keys():
    #     print(each_Country)

    # for population in countries_Population.values():
    #     print(population)


if __name__ == "__main__":
    run()

def likes(names):
    if len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])