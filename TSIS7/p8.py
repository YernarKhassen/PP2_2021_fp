import pygame
import math

pygame.init()


width = 990
height = 490
win = pygame.display.set_mode((1100,600))

pygame.display.set_caption("tsis7")

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
BLUE = [0,0,255]

x = 50
y = 50

tt_size = 49
tt_size2 = 165


def drawOsi():
    pygame.draw.line(win,BLACK,((width/2)+x,y),((width/2)+x,height+y),3)
    pygame.draw.line(win, BLACK, (x,(height/2)+y), (width+x, (height/2)+y), 3)


def drawGrid():

    for line in range(0,12):
        pygame.draw.line(win, (BLACK), (x, y+line * tt_size), (width+x, y+line * tt_size))
        pygame.draw.line(win, (BLACK), (x+line * tt_size2, y), (x+line * tt_size2, height+y))

    for line in range(height):

        pygame.draw.line(win,(BLACK),(x+2,y+line*(tt_size/2)),(x+9,y+line * (tt_size/2)))
        pygame.draw.line(win,(BLACK),(x+2,y+line*(tt_size/4)),(x+6,y+line * (tt_size/4)))

        pygame.draw.line(win,(BLACK),(width+x-9,y+line*(tt_size/2)),(width+x-2,y+line * (tt_size/2)))
        pygame.draw.line(win,(BLACK),(width+x-6,y+line*(tt_size/4)),(width+x-2,y+line * (tt_size/4)))

    for line in range(width):

        pygame.draw.line(win, (BLACK), (x+line * (tt_size2/2), y+2), (x+line * (tt_size2/2), y+16))
        pygame.draw.line(win, (BLACK), (x+line * (tt_size2/4), y+2), (x+line * (tt_size2/4), y+9))
        pygame.draw.line(win, (BLACK), (x+line * (tt_size2/8), y+2), (x+line * (tt_size2/8), y+5))

        pygame.draw.line(win, (BLACK), (x+line * (tt_size2 / 2), height+y-16), (x+line * (tt_size2 / 2), height+y-2))
        pygame.draw.line(win, (BLACK), (x+line * (tt_size2 / 4), height+y-9), (x+line * (tt_size2 / 4),  height+y-2))
        pygame.draw.line(win, (BLACK), (x+line * (tt_size2 / 8), height+y-6), (x+line * (tt_size2 / 8),  height+y-2))

def drawSin():
    points = []
    n = 6
    A = 196
    for i in range(width):
        k = int(math.sin(i / width * n * math.pi) * A +245) +y
        points.append([i+x,k])
    pygame.draw.aalines(win,RED,False,points,5)
    pygame.display.flip()

def drawCos():

    points = []
    n = 6
    A = 196
    for i in range(width):
        k = int(math.cos(i / width * n * math.pi) * A + 245)+y
        points.append([i+x, k])
    pygame.draw.aalines(win, BLUE, False, points, 5)

def drawPoints():

    arr = ['1.00', '0.75', '0.50', '0.25', '0.00', '-0.25', '-0.50', '0.75', '-1.00']

    z = y
    while z < 500:
        for i in arr:
            font = pygame.font.Font('freesansbold.ttf', 14)
            text = font.render(i, True, BLACK)
            textRect = text.get_rect()
            textRect.center = (20, z)
            win.blit(text, textRect)
            z += tt_size

def drawPoints2():

    arr2 = ['-3п','-5п/2','-2п','-3п/2','-п','-п/2','0','п/2','п','3п/2','2п','5п/2','3п']

    l = x
    while l < 1000:
        for i in arr2:
            font = pygame.font.Font('freesansbold.ttf', 14)
            text = font.render(i, True, BLACK)
            textRect = text.get_rect()
            textRect.center = (l, height + y+20)
            win.blit(text, textRect)
            l += tt_size2/2

def txtSin():

    font = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render('sin', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (750, 110)
    pygame.draw.line(win, RED, (780, 110), (810, 110))
    win.blit(text, textRect)
def txtCos():

    font = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render('cos', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (750, 140)
    pygame.draw.line(win,BLUE,(780,140),(810,140))
    win.blit(text, textRect)

run = True
while run:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False


    win.fill(WHITE)
    pygame.draw.rect(win,BLACK,(x,y,width,height),3)

    drawOsi()
    drawGrid()
    pygame.draw.rect(win, WHITE, (0, 0, x, height + y))
    drawPoints()
    pygame.draw.rect(win, WHITE, (0, height+y+20, x, 500))
    pygame.draw.rect(win,WHITE,(x,height+y,width,height))
    pygame.draw.rect(win, WHITE, (width+x,y,width, height))

    drawPoints2()
    txtSin()
    txtCos()
    drawCos()
    drawSin()

    pygame.display.update()


pygame.quit()