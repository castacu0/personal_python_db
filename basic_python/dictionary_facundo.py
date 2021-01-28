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

      # 3 different ways of using 'strings'
    for each_Country, population in countries_Population.items():
        print("With commas", each_Country, "has:", population, "people." ) #1
        print(each_Country + " has: " + str(population) + " people." ) #2
        print(f"The sexy country named {each_Country} has {population} people.") #3
        print("\n") #This gives me more space. You can erase it.


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