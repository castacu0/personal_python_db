#This is the class keeper

class Student:
    """This is my Student data type.
    The values ending with _Xz are a way to identify them.
    I will print the ones to the left
    ---> self.name    NOT    name_XZ
    print(Student.name)"""

    def __init__(self, name_Xz, faculty_Xz, gpa_Xz, approved_Xz):
         self.name = name_Xz
         self.faculty = faculty_Xz
         self.gpa = gpa_Xz
         self.approved = approved_Xz

print(help(Student))