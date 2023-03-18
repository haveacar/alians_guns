import pygame.font

class Scores:
    """Display game statistic"""

    def __init__(self, screen, stats):
        self.screen= screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139,195, 74)
        self.font = pygame.font.SysFont("Comic Sans MS", 38)
        self.image_score()

    def image_score(self):
        """Rend text to graphic"""
        self.score_img =self.font.render(str(self.stats.score), True, self.text_color, (0,0,0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right -40
        self.score_rect.top = 20


    def show_score(self):
        """show score on screen"""
        self.screen.blit(self.score_img, self.score_rect)