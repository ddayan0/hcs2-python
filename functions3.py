# Dennis Dayan, Watson 3B, Functions3.py
x = 24
y = 11
z = 2
print(x)
print(y)
print(z)

def xFun():
    x = 24
    print(x)

xFun()

def yFun():
    y = 11
    print(y)

yFun()

def zFun():
    z = 2
    print(z)

zFun()

def xChange(num1):
    global x
    x = num1
    print("new local x is", num1)
    print("new global x is", num1)
xChange(15)

def yChange(num2):
    global y
    y = num2
    print("new local y is", num2)
    print("new global y is", num2)

yChange(30)

def zChange(num3):
    global z
    z = num3
    print("new local z is", num3)
    print("new global z is", num3)

zChange(45)


print(x)
print(y)
print(z)
