def TodayDate2(m, d, y):
    print m, d, y

TodayDate2(9, 27, 2018)

def ageCalc(month, date, year):
    if (month < 9):
        myAge = 2018 - year
    else:
        myAge = 2018 -(year+1)
    print"My birthday is", month, "/", year, "and I'm", myAge, "years old!"
ageCalc(11, 24, 2002)

def F2C(ftemp):
    x = (ftemp - 32)*.5556
    print(x)

def C2F(ctemp):
    f = (ctemp*1.8)+32
    print(f)

C2F(5)
F2C(5)
