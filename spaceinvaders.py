#lest we hope god grants the end to this pygame hell swiftly
#can we just do java already
#like, i don't even know java and i want to do it at this point
#gofd can this end
#I legit had a pygame nightmare

#Dennis Dayan
#spaceincaders.py #honestly  i dont even care that i misspelled that

#comments mean the same in level 2

import pygame #imports pygame
import sys #Imports sys
import time #imports time
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((800, 600))
x = 25 #global x
y = 540 #global y
width = 40 #global
height = 60 #global
vel = 5 #globaal
# enemyx = 40
# enemyy = 40
score = 0

#Enter music here
pygame.mixer.init()
pygame.mixer.music.load('ps1.mp3')#any mp3 file
pygame.mixer.music.play()









def draw(): #draws ships, projectiles, calls score function
    screen.blit(ship.image, (x, y))
    for i in projlist:
        i.draw(screen)
    for i in enemyList:
        i.draw(screen)
    Score()
    pygame.display.update()


def redrawCollision(): #Handles collisions with projectiles and enemies, handles level two as well

    for p in projlist:
        p.draw(screen)
        p.rect = pygame.Rect(p.x, p.y, p.size, p.size)
        for i in enemyList:
            if(p.collision(i)):
                del enemyList[enemyList.index(i)]
                global score
                score += 1
                pygame.mixer.pre_init(44100, 16, 2, 4096)
                hitsound = pygame.mixer.Sound('mgs.wav')
                hitsound.play()
                if score >= 13:
                    levelTwo()

                #enter collide music here






def Score(): #Does not add score, only displays
    scoremessage = 'Score : {} '.format(score)
    textsurface = myfont.render(scoremessage, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))







def levelTwo(): #calls level 2
   import os
   os.system("python spaceinvaderslvl2.py")

clock = pygame.time.Clock()
pygame.mouse.set_visible(0) #sets mouse not visible
running = True

#Initializes characters
ship = pygame.sprite.Sprite()
ship.rect = pygame.Rect(40, 40, 40, 40) #(X, Y, H, W) #Change these
shipfile = pygame.image.load('ship.png')
ship.image = shipfile


# enemy = pygame.sprite.Sprite()
# enemy.rect = pygame.Rect(40, 40, 40, 40)
# enemyfile = pygame.image.load('ramsticks.jpg')
# enemy.image = enemyfile


#END OF CHAR INIT
class Enemy(): #Class for enemy, code is self-explanatory
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.self = pygame.sprite.Sprite()
        self.rect = pygame.Rect(x, y, size, size)
        image = pygame.image.load('ramsticks.jpg')
        image = pygame.transform.scale(image, (size, size))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
enemyList = [] #list for enemys

#Code below draws enemies onto the screen
for i in range(80, 680, 100):
    enemyList.append(Enemy(i, 50, 50))
for i in range(30, 730, 100):
    enemyList.append(Enemy(i, 150, 50))







projlist = [] #Projectile list for spawining them in
class Projectile(object): #Class for projectiles, self explanatory
    def __init__(self, x,y,width):
        self.x = x
        self.y = y
        self.size = width
        self.vel = 10 #DO NOT CHANGE
        self.self = pygame.sprite.Sprite()
        self.rect = pygame.Rect(x, y, width, width)
        image = pygame.image.load('projectile.png')
        image = pygame.transform.scale(image, (5, 5))
        self.image = image
    def draw(self, screen):
        screen.blit(self.image, (self.x-1, self.y-1))
    def collision(self, obj):
        if pygame.sprite.collide_rect(self,obj):
            return True
        return False
theClock = pygame.time.Clock()

background = pygame.image.load('macosx.jpg')



while running:
    clock.tick(60) #60FPS OR BUST
    screen.blit(background, (0,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for projectile in projlist: #Handles projectiles off screen
        if projectile.y > 0:
            projectile.y -= vel
        else:
            del projlist[-1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit(0)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 700 - vel - width:
        x += vel
    if keys[pygame.K_SPACE]:
        projlist.append(Projectile(x, y, 10))



# put collision method here
#     for projectile in projlist:
#         for enemy in enemyList:
#           if Projectile.collision(projectile, Enemy): #NEED TO FIX,
#               print('Collision')



    screen.blit(ship.image, (x, y))

    ship.rect = pygame.Rect(x, y, 40, 40) #(X, Y, H, W) #Change these

    draw()
    redrawCollision()
    #redrawCreatures()
    pygame.display.update()

#wrap program in function and make level 2

