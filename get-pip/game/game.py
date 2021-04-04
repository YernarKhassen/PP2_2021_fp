import pygame
from pygame.locals import *
pygame.init()

win_width = 600
win_height = 390
win = pygame.display.set_mode((win_width,win_height))

pygame.display.set_caption("Dota3")


walkRight = [pygame.image.load('Walk (1).png'), pygame.image.load('Walk (2).png'), pygame.image.load('Walk (3).png'),pygame.image.load('Walk (4).png'),pygame.image.load('Walk (5).png'),pygame.image.load('Walk (6).png'),pygame.image.load('Walk (7).png'),pygame.image.load('Walk (8).png'),pygame.image.load('Walk (9).png'),pygame.image.load('Walk (10).png')]
walkLeft = [pygame.image.load('Left (1).png'), pygame.image.load('Left (2).png'), pygame.image.load('Left (3).png'),pygame.image.load('Left (4).png'),pygame.image.load('Left (5).png'),pygame.image.load('Left (6).png'),pygame.image.load('Left (7).png'),pygame.image.load('Left (8).png'),pygame.image.load('Left (9).png'),pygame.image.load('Left (10).png')]
playerStd = pygame.image.load('Idle (8).png')

bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()

tt_size = 30
hg = 55
wd = 41
x = 60
y = win_height-55
sp = 5


isJump = False
jumpCount = 10

left = False
right = False
aniCount = 0
lastMove = "right"

class pumpkin():

    def __init__(self, x, y, rad, color,facing):

        self.x = x
        self.y = y
        self.rad = rad
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def drow(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.rad)

def drawGrid():
    for line in range(0,20):
        pygame.draw.line(win,(255,255,255),(0,line*tt_size),(win_width, line * tt_size))
        pygame.draw.line(win,(255,255,255),(line*tt_size,0),(line * tt_size,win_height))


class World():
    def __init__(self,data):

        self.tile_list = []

        dirt_img = pygame.image.load('dirt.jpg')
        grass_img = pygame.image.load('grass.jpg')


        r_cnt = 0
        for row in data:
            c_cnt = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(tt_size,tt_size))
                    img_rect = img.get_rect()
                    img_rect.x = c_cnt*tt_size
                    img_rect.y = r_cnt*tt_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img,(tt_size,tt_size))
                    img_rect = img.get_rect()
                    img_rect.x = c_cnt*tt_size
                    img_rect.y = r_cnt*tt_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)

                c_cnt += 1
            r_cnt+=1

    def draw(self):
        for tile in self.tile_list:
            win.blit(tile[0],tile[1])
            pygame.draw.rect(win,(255,255,255),tile[1],1)

world_data =[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
world = World(world_data)
def drowWin():

    global aniCount
    win.blit(bg, (0, 0))

    world.draw()

    # drawGrid()

    if aniCount+1>=30:
        aniCount = 0

    if left:
        win.blit(walkLeft[aniCount // 5], (x,y))
        aniCount+=1
    elif right:
        win.blit(walkRight[aniCount // 5], (x,y))
        aniCount+=1
    else:
        win.blit(playerStd, (x,y))

    for pump in pumpkins:
        pump.drow(win)

    pygame.draw.rect(win,(255,255,255),(x,y,wd,hg),1)
    pygame.display.update()


pumpkins = []

run = True
while run:
    clock.tick(30)


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False

    for pump in pumpkins:
        if pump.x < 580 and pump.x > 0:
            pump.x += pump.vel
        else:
            pumpkins.pop(pumpkins.index(pump))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:

        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(pumpkins) < 8:
            pumpkins.append(pumpkin(round(x + wd // 2),round(y + hg // 2), 5, (255,165,0), facing))

    if keys[pygame.K_LEFT] and x > 20 :
        x -= sp
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 600 - wd - 3:
        x += sp
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        aniCount = 0
        lastMove = "right"

    if not(isJump):

        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            isJump = True

    else:
        if jumpCount>=-10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 6
            else:
                y -= (jumpCount ** 2) / 6
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10




    drowWin()



pygame.quit()
