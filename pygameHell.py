# lets hope this works....
# it worked!
# Dennis Dayan
# You ever think about the last time you played videogames with an online friend, and you both say see you later but its been 3 years since they've been online?
print("pygame gods mercy me") #Just an appeal to the pygame gods to help me through this hellish journey
import pygame #Gave me essential pygame functions
import sys   #allows me to gracefully exit
pygame.init() #initalises pygame itself (duh)
pygame.mixer.pre_init(44100, 16, 2, 4096) #Sets parajeters such as frequency for my sound)
pygame.mixer.init() #Initalizes pygame mixer to allow me to play sound
pygame.mixer.music.load('bgmusic.mp3') #Loads music
pygame.mixer.music.play(999) #Plays music
pygame.init() #See Line 8, and if you cant see I would not recommend trying to play this game
win = pygame.display.set_mode((580, 434)) #Sets dimensions of display (sorry its not 4k hdr)
pygame.display.set_caption("pay ur taxes jeff") #Witty caption that im known for
#Disregard the two dissapoinments on line 18-19
#walkRight = [pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png')]
#walkLeft = [pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png'), pygame.image.load('TheIRS.png')]
bg = pygame.image.load('Amazon-logo.png') #Loads background image
##---------------------------------- BELOW IS CODE FOR MAKING THE CHARACTERS
char = pygame.sprite.Sprite()   #Sets char as a sprite for collision method
char.rect = pygame.Rect(0, 0, 70, 67)  #Imma keep it real with u Mr. Watson, I forgot what this does
charfile = pygame.image.load('TheIRS.png') #Loads image for character
char.image = charfile #Sets 24 to a var for ease
robber = pygame.sprite.Sprite() #Sets robber to a sprite for collision method
import random #imports random for the sprite to move around the screen randomly
#randx = random.randint(0, 200) #Ignore
#randy = random.randint(0, 200)  #Ignore
robx = random.randint(0, 434) #Robx to a random number from 0 to 434
roby = random.randint(0, 434) #Same as above but with y
robber.rect = pygame.Rect(80, 80, robx, roby) #See line 24
robberfile = pygame.image.load('bezos.jpg') #Sets image for robber
robber.image = robberfile #Sets 33 to a var for ease
screenWidth = 495 #Sets a appropriate screen width
##------------------------------------ END!

#ALL CODE BELOW IS JUST SETTING DIMENSIONS/PARAMETERS
x = 0
y = 0
width = 64
height = 64
velocity = 20
clock = pygame.time.Clock()
run = True
score = 0
#robx = random.randint(0, 480)
#roby = random.randint(0, 480)
# ---------------------------------- END





def redrawGameWindow():
    win.blit(bg, (0,0)) #Displays background
    win.blit(char.image, char.rect.topleft) #Displays char
    win.blit(robber.image, robber.rect.topleft) #Displays robber


#------------------------ START OF FAILED LINES
    #win.blit(robber.image, (randx, randy))
    #win.blit(charfile, charfile.get_rect())

    #need to add spirtes over here
    #-------------------------END OF FAILED LINES

    pygame.display.update() #Updates entire display


#need to add collision method down here, (DONE!)
while run:  #while loop
    clock.tick(60) #6o FPS AAAHHHHHHH!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity: #Moves char left
        x -= velocity
        #left = True
        #right = False
    if keys[pygame.K_RIGHT] and x < screenWidth - velocity - width: #Moves char right
        x += velocity
        #right = True
        #left = False
    if keys[pygame.K_UP] and y > velocity: #Moves char up
        y -= velocity
        #right = False
        #left = False
    if keys[pygame.K_DOWN] and y < screenWidth - height - velocity: #Moves char down
        y += velocity
        #right = False
        #left = False

    win.blit(bg, (0,0)) #Displays Background
    win.blit(char.image, (x, y)) #Displays char
    win.blit(robber.image, robber.rect.topleft) #Imma keep it real with u Mr Watson, I have no idea what this does
    char.rect = pygame.Rect(x, y, 70, 67)
    #robber.rect = pygame.Rect(80, 80, robx, roby)
    if pygame.sprite.collide_rect(char,robber ): #Start of my absolutely amazing collision method
        robbersound = pygame.mixer.Sound('mgs.wav') #Plays MGS Alert sound when collided to alert the user in an extremely comical nature
        robbersound.play() #Plays sound
        print("Your Score is {}".format(score)) #Prints Score
        score += 1 #Adds score when collided
        robber.rect.x = random.randrange(0, 434)  #Sets robber x when hit
        robber.rect.y = random.randrange(0, 434)   #Sets robber y when hit
        if score > 25: #Dispplays game over message
            print('''

 ________  __    __  ________        ______      _______       ______          ______   __        __       __   ______  __      __   ______         __       __  ______  __    __   ______
|        \|  \  |  \|        \      |      \    |       \     /      \        /      \ |  \      |  \  _  |  \ /      \|  \    /  \ /      \       |  \  _  |  \|      \|  \  |  \ /      \
 \$$$$$$$$| $$  | $$| $$$$$$$$       \$$$$$$    | $$$$$$$\   |  $$$$$$\      |  $$$$$$\| $$      | $$ / \ | $$|  $$$$$$ $$\  /  $$|  $$$$$$\      | $$ / \ | $$ \$$$$$$| $$\ | $$|  $$$$$$
   | $$   | $$__| $$| $$__            | $$      | $$__| $$   | $$___\$$      | $$__| $$| $$      | $$/  $\| $$| $$__| $$ \$$\/  $$ | $$___\$$      | $$/  $\| $$  | $$  | $$$\| $$| $$___\$$
   | $$   | $$    $$| $$  \           | $$      | $$    $$    \$$    \       | $$    $$| $$      | $$  $$$\ $$| $$    $$  \$$  $$   \$$    \       | $$  $$$\ $$  | $$  | $$$$\ $$ \$$    \
   | $$   | $$$$$$$$| $$$$$           | $$      | $$$$$$$\    _\$$$$$$\      | $$$$$$$$| $$      | $$ $$\$$\$$| $$$$$$$$   \$$$$    _\$$$$$$\      | $$ $$\$$\$$  | $$  | $$\$$ $$ _\$$$$$$
   | $$   | $$  | $$| $$_____        _| $$_  __ | $$  | $$ __|  \__| $$      | $$  | $$| $$_____ | $$$$  \$$$$| $$  | $$   | $$    |  \__| $$      | $$$$  \$$$$ _| $$_ | $$ \$$$$|  \__| $
   | $$   | $$  | $$| $$     \      |   $$ \|  \| $$  | $$|   $$    $$      | $$  | $$| $$     \| $$$    \$$$| $$  | $$   | $$     \$$    $$      | $$$    \$$$|   $$ \| $$  \$$$ \$$    $
    \$$    \$$   \$$ \$$$$$$$$       \$$$$$$ \$$ \$$   \$$ \$$ \$$$$$$        \$$   \$$ \$$$$$$$$ \$$      \$$ \$$   \$$    \$$      \$$$$$$        \$$      \$$ \$$$$$$ \$$   \$$  \$$$$$$



 _______    ______  __      __        __      __   ______   __    __  _______         ________   ______   __    __  ________   ______   __
|       \  /      \|  \    /  \      |  \    /  \ /      \ |  \  |  \|       \       |        \ /      \ |  \  |  \|        \ /      \ |  \
| $$$$$$$\|  $$$$$$ $$\  /  $$       \$$\  /  $$|  $$$$$$\| $$  | $$| $$$$$$$\       \$$$$$$$$|  $$$$$$\| $$  | $$| $$$$$$$$|  $$$$$$\| $$
| $$__/ $$| $$__| $$ \$$\/  $$         \$$\/  $$ | $$  | $$| $$  | $$| $$__| $$         | $$   | $$__| $$ \$$\/  $$| $$__    | $$___\$$| $$
| $$    $$| $$    $$  \$$  $$           \$$  $$  | $$  | $$| $$  | $$| $$    $$         | $$   | $$    $$  >$$  $$ | $$  \    \$$    \ | $$
| $$$$$$$ | $$$$$$$$   \$$$$             \$$$$   | $$  | $$| $$  | $$| $$$$$$$\         | $$   | $$$$$$$$ /  $$$$\ | $$$$$    _\$$$$$$\ \$$
| $$      | $$  | $$   | $$              | $$    | $$__/ $$| $$__/ $$| $$  | $$         | $$   | $$  | 111$$|  $$ \$$\| $$_____ |  \__| $$ __
| $$      | $$  | $$   | $$              | $$     \$$    $$ \$$    $$| $$  | $$         | $$   | $$  | $$| $$  | $$| $$     \ \$$    $$|  \
 \$$       \$$   \$$    \$$               \$$      \$$$$$$   \$$$$$$  \$$   \$$          \$$    \$$   \$$ \$$   \$$ \$$$$$$$$  \$$$$$$  \$$



            ''')
            sys.exit(0) #Forced graceful exit.

        #robx = randx
        #roby = randy

            #win.blit(robber.image, (randx, randy))
        #sys.exit(0)



    #if score > 10:
        #print("You Won!")
    pygame.display.update() #Updates display

    redrawGameWindow() #Redraws window
    #pygame.display.update()

pygame.quit() #Quits pygame



#whoah u actually read down this far. So uuuhhhh theres nothing down here so....... yeah.




