class Person:

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        return

    def printFullName(self):
        print(f{self.firstname} {self.lastname})


class Student(Person):
    def __init__(self, fname, lname, studID, hg):
        super().__init__(fname, lname)
        self.studentID = studID
        self.houseGroup = hg
        self.subjects = []
        return


    def enrollClass(self, subjectName):
        s1 = Subject()
        s1.subjectName = subjectName
        s1.studentID = studID


    def showClasses(self):
        for i in subjects:
            print(subjects[i])



class Subject():
    def __init__(self)
