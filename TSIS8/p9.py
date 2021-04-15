import pygame
from pygame.locals import *
import random,time
import sys

pygame.init()

win_width = 480
win_height = 640


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
SPEED = 2
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 26)
game_over = pygame.image.load('bg.jpg')


BG = pygame.image.load('bg1.jpg')

clock = pygame.time.Clock()

win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("cooldriving")

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy,self).__init__()
        self.img = pygame.image.load("enemy.png")
        self.surf = pygame.Surface((50,80))
        self.rect = self.surf.get_rect(center = (random.randint(50,430),0))

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 720):
            self.rect.top = 0
            self.rect.center = (random.randint(40,440),0)

    def draw(self,Surface):
        Surface.blit(self.img,self.rect)

class Treasure(pygame.sprite.Sprite):

    def __init__(self):
        super(Treasure,self).__init__()
        self.img = pygame.image.load("nice.png")
        self.surf = pygame.Surface((20,30))
        self.rect = self.surf.get_rect(center = (random.randint(50,430),0))

    def move(self):
        global SCORE
        self.rect.move_ip(0,3)
        if (self.rect.bottom > 720):
            self.rect.top = 0
            self.rect.center = (random.randint(40,440),0)
        elif pygame.sprite.spritecollideany(P1, coins):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 440), 0)
            SCORE+=1

    def draw(self,Surface):
        Surface.blit(self.img,self.rect)

# class Ball(pygame.sprite.Sprite):
#
#     def __init__(self):
#         super(Ball,self).__init__()
#         self.img = pygame.image.load("ball.jfif")
#         self.surf = pygame.Surface((20,30))
#         self.rect = self.surf.get_rect(center=((win_width / 2), 550))
#
#     def draw(self):
#         Surface.blit(self.img, self.rect)
#
#     def move(self):
#
#         keys = pygame.key.get_pressed()
#
#         if self.rect.top > 0:
#             if keys[K_SPACE]:
#                 self.rect.move_ip(0, -3)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.img = pygame.image.load("ship.png")
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center=((win_width / 2), 550))

    def move(self):
        keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if keys[K_LEFT]:
                self.rect.move_ip(-SPEED,0)
        if self.rect.right < win_width:
            if keys[K_RIGHT]:
                self.rect.move_ip(SPEED, 0)

    def draw(self, surface):
        surface.blit(self.img, self.rect)

P1 = Player()
E1 = Enemy()
C1 = Treasure()
# B1 = Ball()
coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprts = pygame.sprite.Group()
all_sprts.add(P1)
all_sprts.add(E1)
all_sprts.add(C1)
# all_sprts.add(B1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

run = True
while run:

    for ev in pygame.event.get():

        if ev.type == INC_SPEED:
            SPEED += 0.2

        if ev.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    win.blit(BG, (0, 0))

    for entity in all_sprts:
        win.blit(entity.img, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):

        pygame.mixer.Sound('Wave Crashing.wav').play()
        time.sleep(0.5)

        win.blit(game_over, (0, 0))
        scores = font_small.render("Your score "+str(SCORE), True, BLACK)
        win.blit(scores,(160,500))
        pygame.display.update()
        for entity in all_sprts:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()


    scores = font_small.render(str(SCORE), True, BLACK)
    win.blit(scores, (10, 10))

    pygame.display.update()
    clock.tick(60)
