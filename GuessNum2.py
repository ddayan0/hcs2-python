#Dennis Dayan Watson 3A
#Guessing Game
running = True
import random
#imports random library
randomNumber = random.randint(1, 101)
TryNum = 0 # TryNum Sequence Taken from Mr. Watsons initial Guessing Game
while running:
    guess = int(input('Enter an integer : '))
    if guess == randomNumber:
        TryNum += 0
        print("You guessed the number!.. and it only took " + str(TryNum) +  " tries")
    elif guess > randomNumber:
        print('Too high,  should not be my responsibility to tell you.')
        TryNum += 1
    else:
        print('Honestly at this point you should just give up, too low!')
        TryNum += 1
else:
    print('While loop has terminated')
