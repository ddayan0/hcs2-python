#file1
#dennis dayan

quote = "Truth is...the game was rigged from the start\n"

wf = open("quote.txt", "w")

wf.write(quote)

wf.close()
# end of part 1

rf = open("quote.txt" , "r")

data = rf.read()

print(data)

rf.close()

# end of part 2

quote2= "Thats gonna be three points\n"

af = open("quote.txt", "a")

af.write(quote2)

af.close()

rf = open("quote.txt" , "r")

data = rf.read()

print(data)

rf.close()
#end of part 3


quote3 = "Kanye West's albums turned bad after he married Kim Kardashian - Nick Strausberg Tucker\n"

def write2File(filename, string):
    wf = open(filename, "w")
    wf.write(string)
    wf.close()

write2File("func.txt", "mr tucker has a bad music taste ")

def readFile(filename):
    rf = open(filename, "r")
    data = rf.read()
    print(data)
    rf.close()
readFile("func.txt")

write2File("another_quote.txt", quote3)
readFile("another_quote.txt")
#end of part 4

quote4 = "you look like finn wolfhart and michael cera - Arielle Madeam"

def append2File(filename, string):
    af = open(filename, "a")
    af.write(string)
    af.close()
append2File("another_quote.txt", quote4)
readFile("another_quote.txt")
#end of part 5

