#Dennis Dayan
#list2.py
numList = [40, 76, 13, 24]

def line():
    print('\n---------')

line()
def printList():
    for i in numList:
        print(i)
printList()
line()

numList.append(66)
numList.append(55)
numList.append(44)
numList.append(33)
numList.append(22)

printList()
line()

del numList[8]
printList()
line()
del numList[7]
printList()
line()


def addFive():
    print('adds five')
    for i in numList:
        i += 5
        print(i)

addFive()
line()

newList = [5, 10, 20, 30]
def multNum():
    print('multiplies all numbers')
    result = 1
    for i in newList:
        result *= i
    return result

print(multNum())
line()



def minNum():
  min = newList[0]
  for i in newList:
      if i < min:
          min = 1
      return min


print(minNum())
line()

def maxNum():
    max = newList[0]
    for i in newList:
        if i > max:
            max = i
    return max


print(maxNum())
line()




