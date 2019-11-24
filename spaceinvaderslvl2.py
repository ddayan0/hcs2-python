#lest we hope god grants the end to this pygame hell swiftly
#can we just do java already
#like, i don't even know java and i want to do it at this point
#gofd can this end
#I legit had a pygame nightmare

#Dennis Dayan
#spaceincaders.py #honestly  i dont even care that i misspelled that


import pygame
import sys
import time
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode((800, 600))
x = 25
y = 540
width = 40
height = 60
vel = 5
# enemyx = 40
# enemyy = 40
score = 0

# def countdown(n):
#     run = True
#     while run:
#         time.sleep(n)
#         if n== 0:
#             print('TIME IS UP!')









#Enter music here
pygame.mixer.init()
pygame.mixer.music.load('ps1.mp3')#any mp3 file
pygame.mixer.music.play()

name = str(input('Enter Your Name: '))

boom = 10
while boom > 0:
    time.sleep(1)
    print(boom)
    boom -= 1
print("START GAME!")


def draw():
    screen.blit(ship.image, (x, y))
    for i in projlist:
        i.draw(screen)
    for i in enemyList:
        i.draw(screen)
    Score()
    pygame.display.update()

winscreen = pygame.image.load('win.jpg')
def redrawCollision():

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
                # if score >= 13:
                #     for i in range(80, 680, 100):
                #         enemyList.append(Enemy(i, 50, 50))   #this is promising, fix with watsons help
                #     for i in range(30, 730, 100):
                #         enemyList.append(Enemy(i, 150, 50))

                #enter collide music here






def Score():
    scoremessage = 'Score : {} '.format(score)
    textsurface = myfont.render(scoremessage, False, (0, 0, 0))
    screen.blit(textsurface,(0,0))







def redrawCreatures():
   pass

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
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

class Enemy():
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
enemyList = []


for i in range(80, 680, 100):
    enemyList.append(Enemy(i, 50, 50))
for i in range(30, 730, 100):
    enemyList.append(Enemy(i, 150, 50))
for i in range(5, 700, 100):
    enemyList.append(Enemy(i, 250, 50))






#End of Character Initilization
projlist = []
class Projectile(object):
    def __init__(self, x,y,width):
        self.x = x
        self.y = y
        self.size = width
        self.vel = 10
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
    clock.tick(60)
    screen.blit(background, (0,0))


    if score >= 20:
        screen.blit(winscreen, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for projectile in projlist:
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
    redrawCreatures()
    pygame.display.update()

scoreRun = True

while scoreRun:
    if score >= 20:
        file = open("high.txt", "w")
        file.write("{} Scored 20 Points and WON!".format(name))

#wrap program in function and make level 2
