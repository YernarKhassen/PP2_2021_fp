import pygame
from images import *
from pygame.locals import *
import random,time
import sys


pygame.init()


WIN_WIDTH = 665
WIN_HEIGHT = 665
tt_size = 35
FPS = 60
clock = pygame.time.Clock()
font_small = pygame.font.SysFont("Verdana", 26)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
game_over = pygame.image.load('images/game_over.jpg')


win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("жылан")



class Food(pygame.sprite.Sprite):



    def __init__(self):
        super(Food, self).__init__()
        self.img = pygame.image.load("images/apple.png")
        self.surf = pygame.Surface((21,20))
        self.rect = self.surf.get_rect(center=(random.randint(0, 500),random.randint(0, 500)))
    def draw(self,Surface):
        Surface.blit(self.img,self.rect)
        # pygame.draw.rect(Surface,(255,255,255),self.rect,1)
    def move(self):
        if pygame.sprite.spritecollideany(P1, foods):
            self.rect.center = (random.randint(50, 500),random.randint(50, 500))
            P1.is_add = True

    def move2(self):
        if pygame.sprite.spritecollideany(P1, foods):
            self.rect.center = (random.randint(100, 400), random.randint(100, 400))
            P1.is_add = True


class Snake(pygame.sprite.Sprite):

    def __init__(self):
        super(Snake, self).__init__()
        self.size = 1
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center=((50,50)))
        self.head = [pygame.image.load("images/head_down.png"),pygame.image.load("images/head_up.png"),pygame.image.load("images/head_left.png"),pygame.image.load("images/head_right.png")]
        self.body = [pygame.image.load("images/body_VERT.png"),pygame.image.load("images/body_har.png")]
        self.snake_body = [self.rect]
        self.dx = 5
        self.dy = 0
        self.turn = 4
        self.speed = 30
        self.is_add = False

    def draw(self):

        for i in range(0,len(self.snake_body)):
            if i==0:
                if self.turn == 1:
                    win.blit(self.head[0],self.snake_body[i])
                elif self.turn == 2:
                    win.blit(self.head[1],self.snake_body[i])
                elif self.turn == 3:
                    win.blit(self.head[2],self.snake_body[i])
                elif self.turn == 4:
                    win.blit(self.head[3],self.snake_body[i])
            else:
                if self.turn == 1:
                    win.blit(self.body[0],self.snake_body[i])
                elif self.turn == 2:
                    win.blit(self.body[0],self.snake_body[i])
                elif self.turn == 3:
                    win.blit(self.body[1],self.snake_body[i])
                elif self.turn == 4:
                    win.blit(self.body[1],self.snake_body[i])

    def add_to_snake(self):

        self.size += 1

        self.snake_body.append([0,0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 20
        pygame.mixer.Sound('sounds/bite.wav').play()

    def move(self):

        if P1.rect.left < 0:
            P1.rect.right = WIN_WIDTH
        if P1.rect.right > WIN_WIDTH:
            P1.rect.left = 0
        if P1.rect.top < 0:
            P1.rect.bottom = WIN_HEIGHT
        if P1.rect.bottom > WIN_HEIGHT:
            P1.rect.top = 0
        if self.is_add == True:
            self.add_to_snake()

        for i in range(self.size - 1,0,-1):
            self.snake_body[i][0] = self.snake_body[i-1][0]
            self.snake_body[i][1] = self.snake_body[i-1][1]

        self.snake_body[0][0] += self.dx
        self.snake_body[0][1] += self.dy

    def move2(self):

        global game_over

        if P1.rect.left < 30 or P1.rect.right > WIN_WIDTH-30 or P1.rect.top < 30 or P1.rect.bottom > WIN_HEIGHT-30:

            pygame.mixer.Sound('sounds/game_over.mp3').play()
            win.fill(BLACK)
            win.blit(game_over, ((WIN_WIDTH / 2)-180, (WIN_HEIGHT / 2)-116))
            scores = font_small.render("Your score " + str(self.size-1), True, GREEN)
            win.blit(scores, (250, (WIN_HEIGHT / 2)))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        if self.is_add == True:
            self.add_to_snake()

        for i in range(self.size - 1,0,-1):
            self.snake_body[i][0] = self.snake_body[i-1][0]
            self.snake_body[i][1] = self.snake_body[i-1][1]

        self.snake_body[0][0] += self.dx
        self.snake_body[0][1] += self.dy

    def update(self):

        if ev.type == pygame.KEYDOWN:
            if P1.rect.left > 0 and P1.rect.right < WIN_WIDTH:

                if ev.key == pygame.K_RIGHT and P1.dx != -d:
                    P1.dx = d
                    P1.dy = 0
                    P1.turn = 4
                if ev.key== pygame.K_LEFT and P1.dx != d:
                    P1.dx = -d
                    P1.dy = 0
                    P1.turn = 3
            if ev.key == pygame.K_DOWN and P1.dy != -d:
                P1.dx = 0
                P1.dy = d
                P1.turn = 1
            if ev.key == pygame.K_UP and P1.dy != d:
                P1.dx = 0
                P1.dy = -d
                P1.turn = 2

def drawGrid():
    for line in range(0,20):
        pygame.draw.line(win,(255,255,255),(0,line*tt_size),(WIN_WIDTH, line * tt_size))
        pygame.draw.line(win,(255,255,255),(line*tt_size,0),(line * tt_size,WIN_HEIGHT))

class World():

    def __init__(self,data):

        self.tile_list = []


        brick_img = pygame.image.load('images/brick.jpg')
        grass_img = pygame.image.load('images/grass2.png')

        r_cnt = 0
        for row in data:
            c_cnt = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(brick_img,(tt_size,tt_size))
                    img_rect = img.get_rect()
                    img_rect.x = c_cnt*tt_size
                    img_rect.y = r_cnt*tt_size
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 0:
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
world_data1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

]

world_data2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]


world1 = World(world_data1)
world2 = World(world_data2)
all_sprites = pygame.sprite.Group()
P1 = Snake()
F1 = Food()
foods = pygame.sprite.Group()
all_sprites.add(P1)
foods.add(F1)
d = 5
run = True
page = 1
check = False


def drawWin(page):


    global check

    bg1 = pygame.image.load('images/preview/bg1.jfif')
    bg2 = pygame.image.load('images/preview/bg2.jfif')
    bg3 = pygame.image.load('images/preview/bg3.jfif')

    if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_RETURN:
            check = True
    if page == 1:
        win.blit(bg1,(0,0))
        if check == True:
            if P1.size > 2:
                world2.draw()
                P1.update()
                P1.move2()
                F1.move2()
            else:
                world1.draw()
                P1.update()
                P1.move()
                F1.move()
            P1.draw()
            F1.draw(win)
    if page == 2:
        win.blit(bg2,(0,0))
        if check == True:
            world2.draw()
            P1.update()
            P1.move2()
            F1.move2()
            P1.draw()
            F1.draw(win)
    if page == 3:
        win.blit(bg3,(0,0))
        if check == True:
            pygame.quit()
            sys.quit()

while run:


    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            run = False

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_s:
                page+=1
            elif ev.key == pygame.K_w:
                page-=1


    drawWin(page)

    # drawGrid()



    pygame.display.flip()
    clock.tick(P1.speed)
pygame.quit()
