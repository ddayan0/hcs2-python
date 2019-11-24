# Dennis Dayan, Watson 3A
# list1.py

nameList = ['Dennis', 'Arielle', 'Luke', 'Max']
for i in nameList:
    print(i)
print("----------\nFirst name of the list is " + nameList[0])
print(" \nSecond name of the list is " + nameList[1])
print(" \nThird name of the list is " + nameList[2])
print(" \nFourth name of the list is " + nameList[3])
print("~~~~~~~~~~\nLuke can be located at " + (str)(nameList.index('Luke')))
print("_-_-_-_-_-\n")
print('Length of nameList is', (len(nameList)))
print("^^^^^^^^^^\n")

def printList():
    print('Here is my list printed from a function!:')
    for item in nameList:
        print(item)
printList()

print('$$$$$$$$\n')
nameList.append('Bread Sheeran')
nameList.append('Aphex Bread')
nameList.append('Breadye West')

printList()

nameList.remove('Dennis')
nameList.remove('Arielle')
print('$$$$$$$$\n')

printList()

print('%%%%%%%\n')
del nameList[4]

printList()


def messagePrint():
    x1 = nameList[0]
    x2 = nameList[1]
    x3 = nameList[2]
    x4 = nameList[3]
    print(x1, 'is my friend in the I.T. academy along with', x2, '. While in my I.T. classes, I listen to the works of ', x3, 'and', x4, '.')

print('()()()()\n')

messagePrint()



