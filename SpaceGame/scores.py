import pygame.font

class Scores():
    # class to display scores
    def __init__(self, screen, stats):
        # initialize attributes to display scores
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()

    def image_score(self):
        # text rendering in image
        self.score_img = self.font.render('Score: ' + str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        # display scores on the screen
        self.screen.blit(self.score_img, self.score_rect)
