class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        return

    def printFullName(self):
        print(f"{self.firstname} {self.lastname}")


class Student(Person):
    def __init__(self, fname, lname, studID, hg):
        super().__init__(fname, lname)
        self.studentID = studID
        self.houseGroup = hg
        self.subjects = []
        return

    def __str__(self):
        return """"""

    def enrollClass(self, subjectName):
        s1 = Subject(subjectName, self.studentID)
        self.subjects.append



    def showClasses(self):
        for i in subjects:
            print(subjects[i])


class Parent(Person):
    def __init__(self, occupation, alumni):
        self.occupation = occupation
        self.alumni = bool
        

class Subject():
    def __init__(self, subjectName, studentID):
        self.subjectName = subjectName
        self.studentID = studentID

    def printStudentList(self):
        print(studentID)


charlie = Student("Charlie", "Pudsey", 8457368, "Johnson")