import pygame
import math

pygame.init()

win_width = 1000
win_height = 500
win = pygame.display.set_mode((1000,500))

pygame.display.set_caption("hw9")

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
BLUE = [0,0,255]

tt_size = 50
tt_size2 = 167

def txtSin():

    font = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render('sin', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (700, 60)
    pygame.draw.line(win, RED, (730, 60), (760, 60), 3)
    win.blit(text, textRect)

def txtCos():

    font = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render('cos', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (700, 90)
    pygame.draw.line(win,BLUE,(730,90),(760,90),3)
    win.blit(text, textRect)

def drawOsi():
    pygame.draw.line(win,BLACK,(win_width/2,0),(win_width/2,win_height),3)
    pygame.draw.line(win, BLACK, (0,win_height/2), (win_width, win_height/2), 3)

def drawCos():

    points = []
    n = 6
    A = 200
    for x in range(win_width):
        y = int(math.cos(x / win_width * n * math.pi) * A + 250)
        points.append([x, y])
    pygame.draw.lines(win, BLUE, False, points, 3)


def drawSin():
    points = []
    n = 6
    A = 200
    for x in range(win_width):
        y = int(math.sin(x / win_width * n * math.pi) * A +250)
        points.append([x,y])
    pygame.draw.lines(win,RED,False,points,3)
    pygame.display.flip()

def drawGrid():
    for line in range(0,10):

        pygame.draw.line(win,(BLACK),(0,line*tt_size),(win_width, line * tt_size))
        pygame.draw.line(win,(BLACK),(line*tt_size2,0),(line * tt_size2,win_height))

    for line in range(500):

        pygame.draw.line(win,(BLACK),(0,line*(tt_size/2)),(7, line * (tt_size/2)))
        pygame.draw.line(win,(BLACK),(0,line*(tt_size/4)),(4, line * (tt_size/4)))

        pygame.draw.line(win,(BLACK),(1000-7,line*(tt_size/2)),(1000, line * (tt_size/2)))
        pygame.draw.line(win,(BLACK),(1000-4,line*(tt_size/4)),(1000, line * (tt_size/4)))

    for line in range(1000):

        pygame.draw.line(win, (BLACK), (line * (tt_size2/2), 0), (line * (tt_size2/2), 14))
        pygame.draw.line(win, (BLACK), (line * (tt_size2/4), 0), (line * (tt_size2/4), 7))
        pygame.draw.line(win, (BLACK), (line * (tt_size2/8), 0), (line * (tt_size2/8), 3))

        pygame.draw.line(win, (BLACK), (line * (tt_size2 / 2), 500-14), (line * (tt_size2 / 2), 500))
        pygame.draw.line(win, (BLACK), (line * (tt_size2 / 4), 500-7), (line * (tt_size2 / 4), 500))
        pygame.draw.line(win, (BLACK), (line * (tt_size2 / 8), 500-4), (line * (tt_size2 / 8), 500))



run = True
while run:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False


    win.fill(WHITE)
    drawGrid()
    txtSin()
    txtCos()
    drawOsi()
    drawCos()
    drawSin()

    pygame.display.update()


pygame.quit()
