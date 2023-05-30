import pygame, time
from pygame.sprite import Group, Sprite

class Gun(Sprite): # create a child class of Sprite

    def __init__(self, screen):
        # initialize the gun and set its initial position
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('SpaceGame/image/laser_gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        # draw a gun in the current position
        self.screen.blit(self.image, self.rect)

    def update_gun(self): 
        # update the position of the gun according to the flag
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        # create a gun in the center of the bottom side
        self.center = self.screen_rect.centerx

class Bullet(pygame.sprite.Sprite): # create a child class of Sprite
    def __init__(self, screen, gun):
        # create a bullet object at the current position of the gun
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (166, 230, 29)
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # move the bullet up
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draw a bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ino(pygame.sprite.Sprite): # create a child class of Sprite

    def __init__(self, screen):
        # initialize the Ino and set its starting position
        super(Ino, self).__init__() # initialize the parent class of Ino
        self.screen = screen # assign screen to the Ino class
        self.image = pygame.image.load('SpaceGame/image/ino.png') # load image of Ino
        self.image = pygame.transform.scale(self.image, (50, 50)) # scale image of Ino
        self.rect = self.image.get_rect() # get rectangle of Ino
        self.rect.x = self.rect.width # set x coordinate of Ino to the width of the rectangle
        self.rect.y = self.rect.height # set y coordinate of Ino to the height of the rectangle
        self.x = float(self.rect.x) # set x coordinate of Ino to the float of the x coordinate of the rectangle
        self.y = float(self.rect.y) # set y coordinate of Ino to the float of the y coordinate of the rectangle

    def draw(self): 
        # draw Ino at the current position
        self.screen.blit(self.image, self.rect) 

    def update(self): 
        # move Inos 
        self.y += 0.1 # move Ino down
        self.rect.y = self.y # set y coordinate of Ino to the y coordinate of the rectangle


class Scores():
    # class to display scores
    def __init__(self, screen, stats):
        # initialize attributes to display scores
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (166, 230, 29)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_guns()

    def image_score(self):
        # text rendering in image
        self.score_img = self.font.render('Score: ' + str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        # rendering text in image
        self.high_score_img = self.font.render('High score: ' + str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def image_guns(self):
        # display the number of remaining guns
        self.guns = Group()
        for gun_number in range(self.stats.guns_left):
            gun = Gun(self.screen)
            gun.rect.x = 10 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)

    def show_score(self):
        # display scores on the screen
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.guns.draw(self.screen)


class Stats():
    # Initialize statistics
    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('SpaceGame/highscore.txt', 'r') as file_object:
            self.high_score = int(file_object.readline())

    def reset_stats(self):
    # initialize statistics that may change during the game
        self.guns_left = 2
        self.score = 0



# controls of the game
def events(screen, gun, bullets): # Check events of the game
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            # sys.exit()
            pygame.quit()

        elif event.type == pygame.KEYDOWN: # Check if the key is pressed
            # move the gun to the right
            if event.key == pygame.K_RIGHT: 
                gun.mright = True
            elif event.key == pygame.K_LEFT: 
                gun.mleft = True
            elif event.key == pygame.K_SPACE: # Check if the key is SPACE
                new_bullet = Bullet(screen, gun) 
                bullets.add(new_bullet) # Add new bullet to the group of bullets
        elif event.type == pygame.KEYUP: # Check if the key is released
            # stop the gun
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False



# redraw the screen during each pass through the loop # Update screen
def update(bg_img, screen, stats, sc, gun, inos, bullets): 
    screen.blit(bg_img, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets): # Update bullets
    # delete bullets that have disappeared
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True) # Check collisions between bullets and Inos
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gun_kill(stats, screen, sc, gun, inos, bullets):
    # check if the Inos have reached the bottom of the screen
    # game_start(screen, stats, sc)
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:   
        stats.run_game = False
        # sys.exit()
        game_over(screen, stats, sc)

def update_inos(stats, screen, sc, gun, inos, bullets):
    # update the position of all Inos in the army
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos): 
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc, gun, inos, bullets):
    # check whether inos got to the bottom of the screen or not
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

# create an army of Inos
def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) /  ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 3 * ino_height - 100) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)




# Check High Score to Write it into the File
def check_high_score(stats, sc):
    # check if there is a new high score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('SpaceGame/highscore.txt', 'w') as file_object:
            file_object.write(str(stats.high_score))



#  show GAME OVER screen
def game_over(screen, stats, sc):
    # display game over
    # screen.fill((0, 0, 0))
    screen_rect = screen.get_rect()
    font = pygame.font.SysFont(None, 65)
    game_over_image = font.render('GAME OVER', True, (255, 255, 255), (0, 0, 0))
    game_over_rect = game_over_image.get_rect()
    game_over_rect.center = screen_rect.center
    screen.blit(game_over_image, game_over_rect)
    # press any Key to Resrart
    font = pygame.font.SysFont(None, 42)
    restart_image = font.render('Press any Key to Restart', True, (255, 255, 255), (0, 0, 0))
    restart_rect = restart_image.get_rect()
    restart_rect.center = screen_rect.center
    restart_rect.y += 100
    screen.blit(restart_image, restart_rect)
    pygame.display.flip()
    stats.run_game = False
    # sys.exit()
    # pygame.quit()




# ---------------------------------------------RUN THE GAME----------------------------------------------

def run(): # Main function

    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((700, 800)) # Create screen
    pygame.display.set_caption("Space Game") # Set caption
    bg_img = pygame.image.load("SpaceGame/image/bg_stars.jpeg") # Load background image
    gun = Gun(screen) # Create gun
    bullets = Group() # Create group of bullets
    inos = Group() # Create group of Inos
    create_army(screen, inos) # Create army of Inos
    stats = Stats() # Create stats
    sc = Scores(screen, stats) # Create scores

    while True: # Main loop of the game
        
        events(screen, gun, bullets) # Check events of the game 
        if stats.run_game: # Check if the game is running 
            gun.update_gun() # Update gun position
            update(bg_img, screen, stats, sc, gun, inos, bullets) # Update screen
            update_bullets(screen, stats, sc, inos, bullets) # Update bullets
            update_inos(stats, screen, sc, gun, inos, bullets) # Update Inos 
        else:
            if any(event.type == pygame.KEYDOWN for event in pygame.event.get()): # Check if any key is pressed
                stats.run_game = True # Set run_game to True
                stats.reset_stats() # Reset stats
                run() # Run main function

run() # Run the game
