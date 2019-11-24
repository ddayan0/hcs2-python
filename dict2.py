#Dennis Dayan
#Dict2.py

def line():
    print('\n-------------------------')
class_roster_dictionary = {1: {'name':'Matthew', 'age':15, 'favSubject': 'Math'}, 2:{'name': 'Jessica', 'age': 15, 'favSubject': 'English'}}
class_roster_dictionary2 = {1: {'name':'Matthew', 'age': 15, 'favSubject': 'Math'},
                            2: {'name': 'Jessica', 'age': 15, 'favSubject': 'English'}}
class_roster = {
    1: {
        'name': 'Matthew',
        'age': 15,
        'favSubject': 'Math',
        'totalClasses': 5
    },
    2: {
        'name': 'Jessica',
        'age': 15,
        'favSubject': 'English',
        'total classes': 5
    }
}
line()
print(class_roster[1])
line()
print(class_roster[1]['name'])
line()
for i in class_roster:
    name = class_roster[i]['name']
    age = class_roster[i]['age']
    fav = class_roster[i]['favSubject']
    print('{}: {} is {} years old and loves {}'.format(i, name, age, fav))
line()
def printClassRoster():
    for i in class_roster:
        name = class_roster[i]['name']
        age = class_roster[i]['age']
        fav = class_roster[i]['favSubject']
        print('{}: {} is {} years old and loves {}'.format(i, name, age, fav))
printClassRoster()
line()
def printDICT(x): #Same as func above but you can print any dict(for now)
    for i in x:
        name = x[i]['name']
        age = x[i]['age']
        fav = x[i]['favSubject']
        print('{}: {} is {} years old and loves {}'.format(i, name, age, fav))
printDICT(class_roster_dictionary)
line()
class_roster[1]['favSubject'] = 'Computer Science'
printDICT(class_roster)
line()
a = class_roster[2]['age']
del class_roster[2]['age']
b = a + 1
class_roster[2]['age'] = b
printDICT(class_roster)
line()
#def newPrintClassRoster(x):
     #name = x[i]['name']
        #age = x[i]['age']
        #fav = x[i]['favSubject']
        #total = x[i]['total classes']
        #print('{}: {} is {} years old and loves {}. He has {} classes.'.format(i, name, age, fav, total))
#newPrintClassRoster(class_roster)
#Above function does not work, FIX IT DENNIS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
