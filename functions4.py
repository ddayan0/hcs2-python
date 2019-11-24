#Dennis Dayan, Watson 3B, Functions4.py
name = ""
verb = ""
place = ""
food = ""

def myNames(a):
    global name
    name = a
def myVerb(a):
    global verb
    verb = a
def myPlace(a):
    global place
    place = a
def myFood(a):
    global food
    food = a

myNames("Mike")
myVerb("ran")
myPlace("the store")
myFood("pizza.")


def myStory():
    print name, verb, "to", place, "and ate", food

myStory()

