class Students:
    def __init__ (self, firstName, lastName, facultyNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.facultyNumber = facultyNumber

    def __str__(self):
        return 'Student('+str(self.fnum)+', '+self.name+', '+str(self.mark)+')'

class StudentGroup:
    def __init__ (self):
        self.group = []

    def add_student(self,student):
        self.group.append(student)

    def average_mark(self):
        sum = 0
        for student in self.group:
            sum += student.mark
        return round(sum/len(self.group), 2)

    def minimum_mark(self):
        min = self.group[0]
        for student in self.group:
            if min.mark > student.mark:
                min = student
        return min

    def maximum_mark(self):
        max = self.group[0]
        for student in self.group:
            if max.mark < student.mark:
                max = student
        return max

st1 = Student(123, 'Ivan', 5.66)
st2 = Student(122, 'Petyr', 5.32)
st3 = Student(223, 'Dimityr', 5.44)
st4 = Student(222, 'Lili', 5.21)
st5 = Student(323, 'Georgi', 5.11)
st6 = Student(322, 'Maria', 5.13)
group = StudentGroup()

print(group)
group.add_student(st1)
print(group)
group.add_student(st2)
print(group)
group.add_student(st3)
group.add_student(st4)
group.add_student(st5)
group.add_student(st6)
print(group)
print(group.average_mark())
print(group.minimum_mark())
print(group.maximum_mark())



 
    

