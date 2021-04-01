import pygame
import math

pygame.init()

width = 1000
height = 500
win = pygame.display.set_mode((1100,600))

pygame.display.set_caption("tsis7")

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
BLUE = [0,0,255]

x = 50
y = 50

tt_size = 50
tt_size2 = 167


def drawOsi():
    pygame.draw.line(win,BLACK,(rect.get/2,0),(win_width/2,win_height),3)
    pygame.draw.line(win, BLACK, (0,win_height/2), (win_width, win_height/2), 3)





run = True
while run:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False


    win.fill(WHITE)
    pygame.draw.rect(win,BLACK,(x,y,width-10,height-10),5)



    pygame.display.update()


pygame.quit()