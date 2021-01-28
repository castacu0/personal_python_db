"""International Students in the US"""

students = {
    'Belgique' : '75',
    'Mexique' : '4',
    'Bresil' : '1',
    'Canada' : '26',
}

for key1, value2 in students.items(): 
    if value2 == '1':
        sing_or_plur = 'is'
        s = ""
    else:
        sing_or_plur = 'are'
        s = "s"
    print(f'In {key1} there {sing_or_plur} {value2} student{s}.')