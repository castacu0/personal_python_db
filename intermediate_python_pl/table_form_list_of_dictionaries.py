import tabulate
dataset =[{'Major': 'Biology', 'GPA': '2.4', 'Name': 'Edward'}, {'Major': 'Physics', 'GPA': '2.9', 'Name': 'Emily'}, {'Major': 'Mathematics', 'GPA': '3.5', 'Name': 'Sarah'}]
header = dataset[0].keys()
rows =  [x.values() for x in dataset]
print tabulate.tabulate(rows, header, tablefmt='grid')