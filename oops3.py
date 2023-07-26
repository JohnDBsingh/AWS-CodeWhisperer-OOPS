









#// simple python oops concept to find 5 students name, rollno, marks of each 5 subjects and print the total , average and grade of each students

import sys

class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def total(self):
        return sum(self.marks)
    def average(self):
        return sum(self.marks)/len(self.marks)
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Marks:",self.marks)
        print("Total:",self.total())
        print("Average:",self.average())
        print("Grade:",self.grade())
        print("Name:",self.name)
        print("Roll no:",self.rollno)
        print("Marks:",self.marks)
        print("Total:",self.total())
        print("Average:",self.average())
        print("Grade:",self.grade())

def main():

    students = []
    for i in range(5):
        print("Enter the details of student",i+1)
        name = input("Enter the name of student: ")
        rollno = input("Enter the rollno of student: ")
        marks = []
        for j in range(5):
            marks.append(int(input("Enter the marks of subject %d: " %(j+1))))
        print()
        students.append(Student(name,rollno,marks))
    for student in students:
        student.display()
        print()
    return 0

if __name__=='__main__':
    sys.exit(main())


