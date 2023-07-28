from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('You WIN', True, (255, 200, 0))
lose = font.render('You LOSE', True, (255, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (65, 65))    
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Wall(sprite.Sprite): 
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.width =     wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT]  and self.rect.x < win_width-80: 
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN]  and self.rect.y < win_height-80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <=  400:
            self.direction = 'right'
        if self.rect.x >= win_width - 80:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed

        else:
            self.rect.x += self.speed


win_width = 700 
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load('background.jpg'), (win_width, win_height))

player = Player('hero.png', 5, win_height-80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(63, 150, 255, 100, 20, 450 , 10) # -
w2 = Wall(63, 150, 255, 100, 450, 450 , 10) # -
w3 = Wall(63, 150, 255, 90, 20, 10 , 350) # !
w4 = Wall(63, 150, 255, 180, 100, 10 , 350) # !
w5 = Wall(63, 150, 255, 270, 20, 10 , 350) # !
w6 = Wall(63, 150, 255, 360 , 100, 10 , 350) # !
w7 = Wall(63, 150, 255, 450, 20, 10 , 350) # !
w8 = Wall(63, 150, 255, 540 , 100, 10 , 350) # !


clock = time.Clock()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if  not finish:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        player.reset()
        monster.reset()
        final.reset()


        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8):
        finish = True
        window.blit(lose, (200, 200))
        kick.play()
    if sprite.collide_rect(player, final):
        finish = True
        money.play()


    display.update()
    clock.tick(60)