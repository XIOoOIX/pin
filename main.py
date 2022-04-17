from pygame import *
from random import randint
win_width = 685
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-pong')
background = transform.scale(image.load('wallpaper.png'), (win_width, win_height))
font.init()
font = font.SysFont('Arial', 40)

lose1 = font.render('ПЕРВЫЙ ПРОИГРАЛ', True, (180,0,0))
lose2 = font.render('ВТОРОЙ ПРОИГРАЛ', True, (180,0,0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y>= 6:
            self.rect.y-= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y<=win_height-130:
            self.rect.y += self.speed_y
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y>= 6:
            self.rect.y-= self.speed_y
        if keys_pressed[K_s] and self.rect.y<=win_height-130:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_y, player_speed_x):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed_y)
        self.speed_x = player_speed_x
    def move(self):
        self.rect.x+= self.speed_x
        self.rect.y+= self.speed_y
        if self.rect.y > win_height-50 or self.rect.y < 0:
            self.speed_y *= -1
balls = [-3,3]
ball=Ball('tennis.png', 325, 200, 40, 40, balls[randint(0,1)], balls[randint(0,1)])
stenka1=Player('rectangle.png', 70, 200, 10, 120, 3)
stenka2=Player('rectangle.png', 600, 200, 10, 120, 3)

game = True
clock = time.Clock()
FPS = 60
finish = False
score = 0
score1 = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        
        if sprite.collide_rect(stenka1,ball) or sprite.collide_rect(stenka2,ball):
            ball.speed_x *=-1
        if ball.rect.x<0:
            finish = True
            window.blit(lose1,(180, 200))
            score1+=1
            
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2,(180, 200))
            score+=1
        
        stenka1.update()
        stenka2.move()
        stenka1.reset()
        stenka2.reset()
        
        ball.reset()
        ball.move()
        text = font.render("Счет:" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 10))
        text1 = font.render("Счет:" + str(score1), 1, (255, 255, 255))
        window.blit(text1, (550, 10))
        
        display.update()
        clock.tick(FPS)
        
        
    else:
        finish = False
        window.blit(background,(0,0))
        ball.rect.x = 325
        ball.rect.y = 200
        stenka1.rect.x = 70
        stenka1.rect.y = 200
        stenka2.rect.x = 600
        stenka2.rect.y = 200
        time.delay(2000)

    