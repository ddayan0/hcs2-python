#Dennis Dayan
#regEx1.py
def line():
    print('--------------------------------')
import re
#part 1
name = "Dennis David Dayan"
matchName = re.match(" Dayan", name)
print(matchName)
line()
searchName = re.search("Dayan", name)
print('searchName: ', searchName)
line()
#part 2
txt = "16"
pattern = re.compile("16")
pattern.search(txt)
print('txt:', pattern.search(txt))
line()
#part 3
txt = "Friday"
pattern = re.compile('day')
if pattern.search(txt):
    print("Found!")
else:
    print("None")
line()
#part 4
pattern = re.compile("[a-z]")
print(pattern.search("the"))
print(pattern.search("quick"))
print(pattern.search("brown"))
line()
pattern = re.compile("[0-9]")
print(pattern.search("2"))
print(pattern.search("4"))
print(pattern.search("6"))
line()
pattern = re.compile('[a-zA-Z0-9]')
def regExChecker(string, pattern):
    if (pattern.search(string)):
        print("Found!")
    else:
        print('None')
regExChecker('RBRHS', pattern)


