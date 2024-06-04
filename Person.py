class Person:
    def __init__(self, name, last_name, age, nationality):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

class Student(Person):
    def __init__(self, name, last_name, age, nationality, university, year_of_study):
        self.university = university
        self.year_of_study = year_of_study
        Person.__init__(self, name, last_name, age, nationality)
        
class Lecturer(Person):
    def __init__(self, name, last_name, age, nationality, university, experience):
        self.university = university
        self.experience = experience
        Person.__init__(self, name, last_name, age, nationality)
        
        
person1=Student("Lili", "Ivanova", 19, "bulgarian", "TU - Sofia", 2021)
person2=Lecturer("Ana", "Ivanova", 40, "bulgarian", "TU - Sofia", 5)
print(person1.name, person1.last_name, ",", person1.age, ",", person1.nationality, ",", person1.university, ",", person1.year_of_study)
print(person2.name, person2.last_name, ",", person2.age, ",", person2.nationality, ",", person2.university, ",", person2.experience)

    

    
    
