from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x ,self.rect.y))   

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > -1:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 615:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        # картинка стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
 
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


wall7 = Wall(0, 255, 0, 250, 490, 210, 10)
wall6 = Wall(0, 255, 0, 150, 0, 200, 10)
wall5 = Wall(0, 255, 0, 425, 100, 120, 10)
wall4 = Wall(0, 255, 0, 460, 100, 10, 400)
wall3 = Wall(0, 255, 0, 150, 0, 10, 390)
wall2 = Wall(0, 255, 0, 250, 100, 10, 400)
wall = Wall(0, 255, 0, 350, 0, 10, 390)     
hero = Player('hero.png', 50, 100, 1)
cyborg = Enemy('cyborg.png', 500, 300, 1)
treasure = GameSprite('treasure.png', 600, 400, 0)


window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700,500))

clock = time.Clock()

font.init()
font = font.SysFont('Arial',70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOU LOSE', True, (255, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

finish = False 
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        wall7.draw_wall()
        wall6.draw_wall()
        wall5.draw_wall()
        wall4.draw_wall()
        wall3.draw_wall()
        wall2.draw_wall()
        wall.draw_wall()
        cyborg.update()
        hero.update()
        hero.reset()
        cyborg.reset()
        treasure.reset()

        if sprite.collide_rect(hero, treasure): 
            window.blit(win, (200,200))
            finish = True
            money.play()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, wall) or sprite.collide_rect(hero, wall2) or sprite.collide_rect(hero, wall3) or sprite.collide_rect(hero, wall4) or sprite.collide_rect(hero, wall5) or  sprite.collide_rect(hero, wall6) or sprite.collide_rect(hero, wall7):
            window.blit(lose, (200,200))
            finish = True
            kick.play()
    clock.tick(200)
    display.update()





