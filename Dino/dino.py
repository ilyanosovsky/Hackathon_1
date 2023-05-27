import pygame
import random

pygame.init()

#Global constants
screen_height = 600
screen_width = 1100

screen = pygame.display.set_mode((screen_width, screen_height))

running = [pygame.image.load('Dino/Images/DinoRun1.png').convert_alpha(),
    pygame.image.load('Dino/Images/DinoRun2.png').convert_alpha()
]

jumping = pygame.image.load('Dino/Images/DinoJump.png').convert_alpha()

bending = [pygame.image.load('Dino/Images/DinoBend1.png').convert_alpha(),
    pygame.image.load('Dino/Images/DinoBend2.png').convert_alpha()
]

large_cactus = [pygame.image.load('Dino/Images/LargeCactus1.png').convert_alpha(), pygame.image.load('Dino/Images/LargeCactus2.png').convert_alpha(), pygame.image.load('Dino/Images/LargeCactus3.png').convert_alpha()
]

small_cactus = [pygame.image.load('Dino/Images/SmallCactus1.png').convert_alpha(), pygame.image.load('Dino/Images/SmallCactus2.png').convert_alpha(), pygame.image.load('Dino/Images/SmallCactus3.png').convert_alpha()
]

bird = [ pygame.image.load('Dino/Images/Bird1.png').convert_alpha(), pygame.image.load('Dino/Images/Bird2.png').convert_alpha()
]

cloud = pygame.image.load('Dino/Images/Cloud.png').convert_alpha()

bg = pygame.image.load('Dino/Images/Track.png').convert_alpha()

class Dinosaur:
    x_pos = 80
    y_pos = 310
    y_pos_bend = 340
    jump_vel = 8

    def __init__(self):
        self.bend_img = bending
        self.run_img = running
        self.jump_img = jumping

        self.dino_bend = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.jump_vel
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, keys):
        if self.dino_bend:
            self.bend()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0
        
        if keys[pygame.K_UP] and not self.dino_jump:
            self.dino_bend = False
            self.dino_run = False
            self.dino_jump = True
        elif keys[pygame.K_DOWN] and not self.dino_jump:
            self.dino_bend = True
            self.dino_run = False
            self.dino_jump = False
        elif not (keys[pygame.K_DOWN] or self.dino_jump):
            self.dino_bend = False
            self.dino_run = True
            self.dino_jump = False

    def bend(self):
            self.image = self.bend_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.x_pos
            self.dino_rect.y = self.y_pos_bend
            self.step_index += 1

    def run(self):
            self.image = self.run_img[self.step_index // 5]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = self.x_pos
            self.dino_rect.y = self.y_pos
            self.step_index += 1

    def jump(self):
            self.image = self.jump_img
            if not self.dino_jump:
                if self.keys[pygame.K_UP]:
                    self.dino_jump = True
                    self.jump_vel = 8 
            else:             
                if self.dino_jump >= -8:
                    if self.dino_jump > 0:
                        self.dino_rect.y -= (self.dino_jump ** 2) / 2
                    else:
                        self.dino_rect.y += (self.dino_jump ** 2) / 2
                    self.jump_vel -= 1
                else: # if self.jump_vel < self.jump_vel:
                    self.dino_jump = False
                    self.jump_vel = 8
                    # self.dino_rect.y = self.y_pos

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        
class Cloud:
    def __init__(self):
          self.x = screen_width + random.randint(800, 1000)
          self.y = random.randint(50, 100)
          self.image = cloud
          self.width = self.image.get_width()
     
    def update(self):
          self.x -= game_speed
          if self.x < - self.width:
               self.x = screen_width + random.randint(2500, 3000)
               self.y = random.randint(50, 100)
     
    def draw(self, screen):
          screen.blit(self.image, (self.x, self.y))

def main():
    global game_speed, x_pos_bg, y_pos_bg, points
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('Dino/Roboto/Roboto-Black.ttf', 20)

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        screen.blit(text, text_rect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = bg.get_width()
        screen.blit(bg, (x_pos_bg, y_pos_bg))
        screen.blit(bg, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(bg, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
        keys = pygame.key.get_pressed()

        player.draw(screen)
        player.update(keys)

        background()

        cloud.draw(screen)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

main()