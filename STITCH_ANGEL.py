import pygame, sys
import pygame.freetype
import random
from pygame.locals import *
pygame.init()
pygame.freetype.init()

WINDOW_SIZE = (1000, 545)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window
dis = pygame.Surface((1000,545))

fonts = pygame.freetype.Font('other\deltarune.ttf', 70)

clock = pygame.time.Clock()

music = pygame.mixer.music.load('other\SOUND-Burning Love.mp3')
switchSound = pygame.mixer.Sound('other\SOUND-switch.wav')

musicImage = pygame.image.load('other\MMmusic.png')
mainMenuImage = pygame.image.load('other\MM.png')
tutorialImage = pygame.image.load('other\TUTORIAL.png')
winImage = pygame.image.load('other\win.png')
loseImage = pygame.image.load('other\lose.png')

groundImage = pygame.image.load('other\GROUND.png')
spikeImage = pygame.image.load('other\O-SPIKE.png')
bigImage = pygame.image.load('other\O-BIG.png')
highImage = pygame.image.load('other\O-HIGH.png')
lowImage = pygame.image.load('other\O-LOW.png')
homeBarImage = pygame.image.load('other\HOME_BAR.png')
glowImage = pygame.image.load('other\Glow.png')
stitchRun = [pygame.image.load('STITCH\STITCH-1.png'), pygame.image.load('STITCH\STITCH-2.png'), pygame.image.load('STITCH\STITCH-3.png'), pygame.image.load('STITCH\STITCH-4.png'), pygame.image.load('STITCH\STITCH-5.png')]
angelRun = [pygame.image.load ('ANGEL\ANGEL-1.png'), pygame.image.load('ANGEL\ANGEL-2.png'), pygame.image.load('ANGEL\ANGEL-3.png'), pygame.image.load('ANGEL\ANGEL-4.png'), pygame.image.load('ANGEL\ANGEL-5.png'), pygame.image.load('ANGEL\ANGEL-6.png'), pygame.image.load('ANGEL\ANGEL-7.png'), pygame.image.load('ANGEL\ANGEL-8.png'), pygame.image.load('ANGEL\ANGEL-9.png'), pygame.image.load('ANGEL\ANGEL-10.png')]
#gameMap =[['0','1','0','2','0','4','0','3','0','0','0','1','0','1','0','0','3','0','2','3','0','0','2','0','0','3','0','0','1','0','0','0','2','0','0','3','0','0','3','0','4','0','0','4','0','2','2','3','0','1','4','3','0','0','0','4','0','0','4','0','1','1','0','0','4','0','0','0','0','0','1','0','0','0','0','0','1','4','0','0','4','0','0','0','3','0','4','4','0','0','0','1','4','1','4','0','0','0','3','0'],
#          ['0','1','0','4','0','4','0','0','0','3','1','0','1','0','1','0','0','0','0','0','0','2','0','2','3','0','3','1','1','0','4','0','4','0','2','0','1','0','0','0','1','0','4','4','0','0','4','0','4','0','1','0','3','3','0','1','1','1','0','0','0','0','0','0','4','0','0','0','1','4','0','3','0','0','0','4','4','0','3','4','0','1','4','1','4','3','0','0','0','0','4','0','4','0','3','0','0','4','4','0']]


G1 = [['0','1','0','2','0','4','0','3','0','0','0','1','0','1','0','0','3','0','2','0'],
      ['0','1','0','4','0','4','0','0','0','3','1','0','1','0','1','0','0','0','0','0']],

G2 = [['0','0','2','0','0','3','0','0','1','0','4','0','0','4','0','2','2','3','0','0'],
      ['0','2','0','2','3','0','3','1','1','0','4','0','4','0','2','1','1','0','3','0']]

G3 = [['4','3','0','0','0','4','0','0','4','0','1','1','0','0','4','0','0','0','0','0'],
      ['1','0','4','4','0','0','4','0','4','0','1','0','3','3','0','1','1','1','0','0']]

G4 = [['1','0','0','0','0','0','1','4','0','0','4','0','0','0','3','0','4','4','0','0'],
      ['0','0','0','0','4','0','0','0','1','4','0','3','0','0','0','4','4','0','3','0']]

G5 = [['0','1','4','1','4','0','0','0','3','0','0','0','0','0','0','3','0','0','4','0'],
      ['0','1','4','1','4','3','0','0','0','0','4','0','4','0','3','0','0','4','4','0']]

gameMap = [G1, G2, G3, G4, G5]
 
click = False

time = 0
r = 60
t = 0
speed = 15


##################################################### MAIN MENU ##################################################### 
def mainMenu():
    isMusic = True
    isHTP = False
    while True:
        mx, my = pygame.mouse.get_pos()
 
        musicButton = pygame.Rect(680, 203, 47, 47)
        HTPButton = pygame.Rect(667, 285, 219, 55)
        quitbutton = pygame.Rect(950, 10, 30, 30)

        if musicButton.collidepoint((mx, my)):
            if click:
                if isMusic == True:
                    isMusic = False
                elif isMusic == False:
                    isMusic = True 
        elif HTPButton.collidepoint((mx, my)):
            if click:
                isHTP = True
        elif quitbutton.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    gameLoop()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        dis.fill ((172, 228, 226))
        dis.blit(groundImage, (0,0))
        dis.blit(groundImage, (240,0))
        dis.blit(groundImage, (480,0))
        dis.blit(homeBarImage, (0,0))
        dis.blit(stitchRun[0], (10, 180))
        dis.blit(angelRun[0], (10, 415))

        dis.blit(mainMenuImage, (0,0))

        if isMusic == True:
            dis.blit(musicImage, (0,0))
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

        if isHTP == True:
            dis.blit(tutorialImage, (10,0))
        
        screen.blit(pygame.transform.scale(dis,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)

    return isMusic, isSE
        
##################################################### GAME FUNTIONS ####################################################
class player (object):
    def __init__ (self, x, y, w, h, c, run):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.run = run
        self.walkcount = 0
        self.jumpCount = 13
        self.hitbox = pygame.Rect(self.x, self.y, self.w, self.h)
        self.yMomentum = 0
        self.isJump = False
        self.isDown = False

    def jump (self, j):
        if self.jumpCount >= -13:
            n = 1
            if self.jumpCount < 0:
                n = -1
            self.y -= (self.jumpCount **2)*j *n
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 13

    def running (self, dis, d, k, scroll):
        if self.walkcount >= d:
            self.walkcount = 0

        dis.blit(self.run[self.walkcount//3],(self.x -15 -scroll, self.y -k))
        self.walkcount += 1


    def square(self, dis):
        pygame.draw.rect(dis, self.c, (self.x -scroll, self.y, self.w, self.h), 3)

def collision_test(rect, tiles, spikes):
    hit_list = []
    spike_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    for spike in spikes:
        if rect.colliderect(spike):
            spike_list.append(spike)
    return hit_list, spike_list

def move(rect, mx, my,tiles, spikes):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False, 'spike':False}
    hit_list, spike_list = collision_test(rect,tiles, spikes)
    
    for tile in hit_list:
        if mx > 0:
            rect.right = tile.left
            collision_types['right'] = True
            
        elif my > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True

        elif my < 0:
            rect.top = tile.bottom
            collision_types['top'] = True

    for spike in spike_list:
        if mx > 0:
            rect.right = spike.left
            collision_types['spike'] = True
            
        elif my > 0:
            rect.bottom = spike.top
            collision_types['spike'] = True

        elif my < 0:
            rect.top = spike.bottom
            collision_types['spike'] = True     
            
    return rect, collision_types

def draw(scroll, m):
    dis.fill ((172, 228, 226))
    for x in range((speed*3600)//200):
        dis.blit(groundImage, (x*240 -scroll -30, 0))

    tiles = []
    spikes = []
    y = 0
    for layer in m:
        x = 0
        for tile in layer:
            if tile == '1':
                dis.blit(spikeImage,(x*441 -scroll, y*238 +45))
                spikes.append(pygame.Rect(x*441 +180 , y*238 +241, 90, 22))
            elif tile == '2':
                dis.blit(bigImage,(x*441 -scroll,y*238 +45))
                tiles.append(pygame.Rect(x*441 +175, y*238 +177, 70, 93))
            elif tile == '3':
                dis.blit(highImage,(x*441 -scroll,y*238 +45))
                tiles.append(pygame.Rect(x*441 +180, y*238 +45, 60, 168))
            elif tile == '4':
                dis.blit(lowImage,(x*441 -scroll,y*238 +45))
                tiles.append(pygame.Rect(x*441 +175, y*238 +220, 80, 50))
            x += 1
        y += 1

    dis.blit(homeBarImage, (0,0))
        
    stitch.running(dis, 15, 25, scroll)
    angel.running(dis, 30, 40, scroll)

    pygame.draw.rect(dis, (140, 154,41), (53, 31, (stitch.x/8505)*861, 18))

    dis.blit(glowImage, (7805 -scroll ,0))
    dis.blit(winImage, (8505 -scroll ,0))

    return tiles, spikes
    
stitch = player(70, 205, 110, 55, (38, 99, 142), stitchRun)
angel = player(70, 460, 110, 55, (223, 130, 180), angelRun)
  
#################################################### GAME LOOP #################################################### 
def gameLoop():
    n = -1
    time = 0
    r = 60
    t = 0
    speed = 15
    scroll = 0
    m = gameMap[random.randrange(4)]

    running = True
    
    while running == True:
        clock.tick(60)
        scroll += (stitch.x -scroll -100)

    #-------------------------------------------------------------------------------------- EVENTS
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_h:
                        r = 0
                    if event.key == K_UP:
                        stitch.isJump = True
                    if event.key == K_SPACE:
                        switchSound.play()
                        n = n*-1
                        stitch.y += 240*n
                        angel.y += -240*n

        if stitch.isJump == True:
            stitch.jump(0.15)
            angel.jump(0.08)

    #-------------------------------------------------------------------------------------- DRAW
        draw(scroll, m) 
        tiles, spikes = draw(scroll, m)

    #-------------------------------------------------------------------------------------- TIME
        if time > t*60:
            t += 1
            r -= 1
        time += 4
        
        textrect = fonts.get_rect(str(r), size = 70)
        fonts.render_to(dis, (500 -(textrect[2]//2), 20), str(r), (0,0,0))
        fonts.render_to(dis, (498 -(textrect[2]//2), 18), str(r), (255, 255, 255))

    #-------------------------------------------------------------------------------------- COLLISIONS    
        SRect = pygame.Rect(stitch.x, stitch.y, stitch.w, stitch.h)
        ARect = pygame.Rect(angel.x, angel.y, angel.w, angel.h)

        SRect, cStitch = move(SRect, stitch.x, stitch.y, tiles, spikes)
        ARect, cAngel = move(ARect, angel.x, angel.y, tiles, spikes)

        if cStitch['right'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cStitch['bottom'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cStitch['top'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cStitch['spike'] == True:
            stitch.x -= 4000
            angel.x -= 4000

        if cAngel['right'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cAngel['bottom'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cAngel['top'] == True:
            stitch.x -= 30
            angel.x -= 30
        elif cAngel['spike'] == True:
            stitch.x -= 4000
            angel.x -= 4000

        if stitch.x <= 0:
            stitch.x = 70
            angel.x = 70
        elif stitch.x > 8505:
            stitch.x = 70
            angel.x = 70
            n = -1
            time = 0
            r = 60
            t = 0
            speed = 15
            scroll = 0
            for i in range(50):
                dis.blit(winImage, (0,0))
                pygame.display.update()
                screen.blit(pygame.transform.scale(dis,WINDOW_SIZE),(0,0))
            break

        #-------------------------------------------------------------------------------------- CONSTENTS
            
        stitch.x += speed
        angel.x += speed

        if r == -1:
            stitch.x = 70
            angel.x = 70
            n = -1
            time = 0
            r = 60
            t = 0
            speed = 15
            scroll = 0
            for i in range(50):
                dis.blit(loseImage, (0,0))
                pygame.display.update()
                screen.blit(pygame.transform.scale(dis,WINDOW_SIZE),(0,0))
            break

        screen.blit(pygame.transform.scale(dis,WINDOW_SIZE),(0,0))
        pygame.display.update()
        
mainMenu()
