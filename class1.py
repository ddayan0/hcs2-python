#class1.py
#Dennis Dayan
#video tutorial below
def line():
    print('---------------------\n')


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)




# print(emp_1.fullname())
# print(emp_2.fullname())
#
# emp_1.fullname()
# print(Employee.fullname(emp_1))
# line()
# #real class1.py starts below


class Student:

    def __init__(self, name, age, favSubject):
        self.name = name
        self.age = age
        self.favSubject = favSubject

    def greeting(self):
        return 'Hi! My name is {}. I am {} years old and my favorite subject is {}.'.format(self.name, self.age, self.favSubject)
    def birthday(self):
        self.age += 1
        return 'Hi! My name is {}. I am {} years old and my favorite subject is {}.'.format(self.name, self.age, self.favSubject)
    def birthYear(self):
        x =  2018 -self.age
        return '{} was born in {}'.format(self.name, x)
dennis = Student('Dennis', 16, 'CompSci')
arielle = Student('Arielle', 15, 'English')
brianna = Student('Brianna', 15, 'History')

# print(dennis.greeting())
# print(arielle.greeting())
# print(brianna.greeting())
# line()
# print(dennis.birthday())
# print(arielle.birthday())
# print(brianna.birthday())
# line()
# print(dennis.birthYear())
# print(arielle.birthYear())
# print(brianna.birthYear())
# line()



