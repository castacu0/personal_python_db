from data import DATA

# In python 3.9 we use pipe | to add dictionaries
# It's like adding lists with +
#This next example is with other python version
old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))


def run():

    all_python_devs = [i["name"]  for i in DATA  if i["language"] == "python" ]
    all_google_workers = [i["age"] for i in DATA if i["organization"] == "Google"]

    for i in all_python_devs: #OR all_googler_workers:
        print(i)

    adults = list(filter(lambda i: i["age"] > 18 , DATA))
    adults = list(map(lambda i: i["age"] , adults))

    old_people = list(map(lambda i: i | {"old": i["age"] > 70},      DATA))
    old_people = list(map(lambda i: {**i, **{"old": i["age"] > 70}}, DATA))

    # For each dictionary, I want you to add a new Key:Value object returning
    # True or False if the person is older than 70
    # This creates a NEW list but with the new values added.

    for i in old_people:
        print(i)  

if __name__ == "__main__":
    run()