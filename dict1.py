# Dennis Dayan
# dict.py
def line():
    print('\n----------------')

colorInt = {1: 'Red', 2: 'Orange', 3: 'Yellow'}
colorString = {'R': 'Red', 'O': 'Orange', 'Y': 'Yellow'}

for i, j in colorInt.items():
    print(str(i)+":", j)
line()
for i, j in colorString.items():
    print(i+":", j)
line()
for i, j in colorInt.items():
    print("Key {} is assigned to {} ".format(i, j))
line()
def printDictionary(dictionary):
    for i, j in dictionary.items():
        print(str(i)+":", j)
print(colorString)
line()

print(colorInt[1])
line()
print(colorString['R'])
line()
print(len(colorString))
line()
print(len(colorInt))

colorInt[4] = 'Magenta'
colorInt[5] = 'Maroon'
colorInt[6] = 'Beige'
colorInt[7] = 'Khaki'
colorInt[8] = 'Off-White'
line()
printDictionary(colorInt)
line()

del colorInt[5]
printDictionary(colorInt)
line()

colorInt.update({3: 'Not Yellow'})
printDictionary(colorInt)
line()

def searchDict(dictionary, search_value):
    print(dictionary [search_value] ,'is at the value YOU searched!')

    #Broken Bonus Function Below
    #if search_value > (len(colorInt)):
        #print('NO VALUES FOUND FOR YOUR SEARCH')
searchDict(colorInt, 4)
line()

