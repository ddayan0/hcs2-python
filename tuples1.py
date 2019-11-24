# Dennis Dayan, Watson 3A
# tuples1.py

def line():
    print('\n-----------------')

def printObj(obj):
    for i in obj:
        print(i)

numTuple = (5, 6, 7, 8)
nameTuple = ('Bobby', 'Mike', 'Sue', 'Maggie')

printObj(numTuple)
line()
printObj(nameTuple)

numList = [55, 66, 77, 88]
nameList = ['Robert', 'Michael', 'Susan', 'Margaret']

line()
printObj(numList)
line()
printObj(nameList)

line()
print(numTuple.index(5))
print(nameTuple.index('Sue'))
line()
print(numList.index(66))
print(nameList.index('Margaret'))
line()


print(numTuple[1])
print(nameTuple[1])
line()
print(numList[1])
print(nameList[1])
line()


def thcheck(obj):
    for i in obj:
        if i == 30:
            print(i)
        else:
            print('30 is not present in', i)

thcheck(numTuple)
line()

print('Michael' in nameTuple)
line()

print(30 in numList)

line()
print('Dennis' in nameList)
line()
numTupleReversed = reversed(numTuple)
printObj(numTupleReversed)
line()
nameTupleReversed = reversed(nameTuple)
printObj(nameTupleReversed)
line()
numListReversed = reversed(numList)
printObj(numListReversed)
line()
nameListReversed = reversed(nameList)
printObj(nameListReversed)
line()

numTupleSorted = sorted(numTuple)
printObj(numTupleSorted)
line()
nameTupleSorted = sorted(nameTuple)
printObj(nameTupleSorted)
line()
numListSorted = sorted(numList)
printObj(numTupleSorted)
line()
nameListSorted = sorted(nameList)
printObj(nameListSorted)
line()


myFavsTuple = ('RyeBread', 'WhiteBread', 'WholeWheat', 'Baguette', 'GarlicBread', 'OliveBread')

printObj(myFavsTuple)
line()

myFavsTupleReversed = reversed(myFavsTuple)
printObj(myFavsTupleReversed)
line()
myFavsTupleSorted = sorted(myFavsTuple)
printObj(myFavsTuple)
line()


def tupleToList(tuple):
    list = []
    for i in tuple:
        list.append(i)
    return list

printObj(tupleToList(myFavsTuple))
line()

