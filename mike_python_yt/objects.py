#This is my main document where I'll be using my 'StudentX.py' file
from StudentX import Student

if __name__ == "__main__":
    student_1 = Student("Frodo","The Fellowship", 3.9, True)

print(student_1.gpa)