създаване на клас с име и свойство:
class MyFirstClass:
x=5

създаване на обект, базиран на създадения клас:
MyFirstObject = MyFirstClass()

достъпване елементите на класа:
print(MyFirstObject.x)

функция конструктор __init__()

class Person:
        def __init__(self,name,age):
                self.name=name
                self.age=age
        def greetings(self):
                print("Hello, my name is "+self.name)
MyPerson=Person("Ivan",35)
MyPerson.greetings()

параметър self

промяна стойностите на свойства на обекти:
    MyPerson.age=40

изтриване свойства на обекти с del:
    del MyPerson.age

изтриване на цели обекти с del:
    del MyPerson

дефиниране на клас без съдърание (pass):
    class Person:
        pass
