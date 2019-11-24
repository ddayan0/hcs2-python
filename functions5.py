#Dennis Dayan,Watson 3A, Func5

def myName():
    return 'Dennis Dayan'
print(myName())

def favColor():
    return 'Blue'
print(favColor())

def myHobby():
    return 'Computers'
print(myHobby())

def F2C(ftemp):
    x = (ftemp - 32)*.5556
    return x
print(F2C(32))

def maxNum(x, y, z):
    if x > y and x > z:
        return x
    elif x == y and x == z:
        return 'The Numbers are Equal'
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z

print(maxNum(5, 9, 39))

def minNum(x, y, z):
    if x < y and x < z:
        return x
    elif x == y and x == z:
        return 'The Numbers are Equal'
    elif y < x and y < z:
        return y
    elif x < z and z < y:
        return z

print(minNum(15, 30, 45))



def combineNum(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x* z
    elif y == "/":
        return x/z

print(combineNum(maxNum(5, 9, 39), "+", minNum(15, 30, 45)))


def avgNum(x, z):
    a = x + z/2
    return a

print(avgNum(10, 12))


