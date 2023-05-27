import pygame.font
from gun import Gun
from pygame.sprite import Group

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

