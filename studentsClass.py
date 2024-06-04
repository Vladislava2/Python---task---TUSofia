class Student:
    def __init__(self, fnum, name, mark):
        self.fnum = fnum
        self.name = name
        self.mark = mark
    def __str__(self):
        return 'Student ('+str(self.fnum)+','+self.name+','+str(self.mark)+')'

class StudentGroup:
    def __init__(self):
        self.group = []
    def add_student(self, student):
        self.group.append(student)
    def remove_student(self, student):
        self.group.remove(student)
    def average_mark (self):
        sum = 0 
        for student in self.group:
            sum = sum + student.mark
        return round(sum/len(self.group),2)
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
    def sort(self):
        for i in range(len(self.group)):
            min = i
            for j in range(i+1, len(self.group)):
                if self.group[min].mark > self.group[j].mark:
                    min = j
            temp = self.group[i]
            self.group[i] = self.group[min]
            self.group[min] = temp
    def __str__ (self):
        out = ' '
        for student in self.group:
            out = out + str(student) + '\n'
        return out
        return str([str(student) for student in self.group])
fnum = int(input("Факултетен номер: "))
name = input("Име: ")
mark = float(input("Оценка: "))
st1 = Student(fnum, name, mark)
print(st1.__str__())
print(st1)
print(st1.__repr__())

st1 = Student(123, "Иван", 5.66)
st2 = Student(124, "Лили", 4.56)
st3 = Student(125, "Мария", 5.45)
st4 = Student(126, "Георги", 3.43)
st5 = Student(127, "Магдалена", 5.67)
st6 = Student(128, "Илия", 5.89)
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
group.sort()
print(group)