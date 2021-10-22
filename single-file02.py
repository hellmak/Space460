"""
        Space 460 /\
            hellmak @ GitHub

copyright 2021
"""
#import
from sys import exit
from pygame import *
import pygame
import random

pygame.init()

"""
art:
    ship:
        /\
    bullet:
        .
    star:
        *, +

"""
#title
display.set_caption("Space 460")

#classes
class Color():
    def __init__(self):
        self.WHITE  =(255,  255,    255 )
        self.BLACK  =(0,    0,      0   )
        self.RED    =(230,0,100)
        self.GRAY   =(153, 153, 153)

        self.bg     = self.BLACK
        self.player = self.WHITE
        self.bullet = self.WHITE
        self.star   = self.GRAY

color   = Color()

class MyScreen():
    def __init__(self):
        self.WIDTH     = 500
        self.HEIGHT    = 500
        self.SIZE      = [self.WIDTH, self.HEIGHT]
        self.CENTER_X  = self.WIDTH/2
        self.CENTER_Y  = self.HEIGHT/2
        self.CENTER    = (self.WIDTH/2, self.HEIGHT/2)
        self.screen    = display.set_mode((self.WIDTH, self.HEIGHT))

    def makeBackground(self):
        self.screen.fill(color.bg)

my_screen    = MyScreen()

class Player():
    def __init__(self):
        self.pos    = [my_screen.CENTER_X,  my_screen.HEIGHT  - 50]
        self.size   = (30,  30)
        self.limit  = [0, (my_screen.WIDTH - self.size[0]), 0, my_screen.HEIGHT] #should be a two layer: ((x min, x max), (y min, y max))
        self.speed  = (5,   0)
        self.box    = Rect(self.pos, self.size)
        self.keys   = key.get_pressed() #this way does not work and I dont know why
        self.auto_fire  = False
        self.kills  = 0
        self.points = 0

    #movement and shooting
    def move(self):
        keys    = key.get_pressed()
        if(keys[K_UP]):
            print("up")
        if  keys[K_LEFT]    and self.pos[0] >= self.limit[0]:
            self.pos[0] -= self.speed[0]
            print("left")
        if  keys[K_RIGHT]   and self.pos[0] <= self.limit[1]:
            self.pos[0] += self.speed[0]
            print("right")


        #Y movement can be added at later stage


    def toggleAutoFire(self): #not currently in use
        if keys[K_y]:
                self.auto_fire = True
                print("on")
        elif keys[K_n]:
                self.auto_fire = False
                print("off")

    def draw(self):
        draw.rect(my_screen.screen, color.player, Rect(self.pos, self.size))
player      = Player()

class PlayerAmmo(object):
    def __init__(self):
        self.pos    = [(player.pos[0] + (player.size[0]/2)), (player.pos[1] - player.size[0] - 1)]
        self.speed  = 2
        self.damage = 1
        self.size   = [5,5]

    def draw(self):
        draw.rect(my_screen.screen, color.bullet, Rect(self.pos, self.size))
player_ammo = PlayerAmmo() #FIXME lazy temp for passing values to Star

class BgStar(object):
    def __init__(self):
        self.size   = [5,5]
        #self.pos    = (random.randint(0, my_screen.WIDTH), self.size[1])
        self.pos    = [random.randint((-10), (my_screen.WIDTH + 11)),-10]
        self.speed  = 2
        self.damage = 1


    def draw(self):
        draw.rect(my_screen.screen, color.RED, Rect(self.pos, self.size))
bg_star = BgStar() #FIXME lazy temp for passing values to Star
"""
class BgStar(object):
    def __init__(self):
        self.size   = [5,5]
        self.pos    = [random.randint(0, my_screen.WIDTH), self.size]
        self.speed  = 2
        self.damage = 1


    def draw(self):
        draw.rect(my_screen.screen, color.bullet, Rect(self.pos, self.size))
bg_star     = BgStar()
"""
enemies     = []
stars       = []
bullets     = []
bullet_clock= 99999
star_clock  = 99999
bullet_fire_rate = 10
running     = True
FONT        = font.SysFont("Verdana", 20) #pygame.
my_clock    = time.Clock()

drawn_objects = [player]

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        #toggle:
        elif evt.type == KEYDOWN: #tells you if event is relatet to keyboard -EMC235
            #toggle auto_fire:
            if evt.key == K_SPACE: #if the type of the event is KEYDOWN that means it has a .key attribute ant it van be any key -EMC235
                player.auto_fire = not player.auto_fire #reverse boolean value
                print(f"boolean auto_fire = {player.auto_fire}")



    #background
    my_screen.makeBackground() #before drawing anything else

    #/add speed/destroy
    if True:
        if len(stars) < 1000 and star_clock > bullet_fire_rate: #max 999 bullets,
            star_clock = 0
            stars.append(BgStar())
    star_clock += 1

    #move stars. destroy stars
    for x in stars:
        if x.pos[1] < my_screen.HEIGHT:
            x.pos[1] += x.speed
        else:
            stars.pop(stars.index(x))

    #draw stars
    for x in stars:
        x.draw()
    #/background




    player.move()

    #player.draw()

    #gun
    #move bullets. destroy bullets
    for bullet in bullets:
        if bullet.pos[1] > 0:
            bullet.pos[1] -= bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    #/add speed/destroy
    if player.auto_fire:
        if len(bullets) < 1000 and bullet_clock > bullet_fire_rate: #max 999 bullets,
            bullet_clock = 0
            bullets.append(PlayerAmmo())
    bullet_clock += 1

    #draw bullets
    for bullet in bullets: #delete
        bullet.draw()
    #/gun

    for drawable in drawn_objects:
        drawable.draw()
    #if(player.auto_fire):
    #    player_ammo.shoot()
    #    player_ammo.pos[1]  -= player_ammo.speed


    display.flip()
    my_clock.tick(60)
quit()
exit()
