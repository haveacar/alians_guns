import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scores:
    """Display game statistic"""

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont("Comic Sans MS", 38)
        self.image_score()
        self.image_high_score()
        self.image_ships()

    def image_score(self):
        """Rend text to graphic"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """Rend text to graphic"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, "Gold", (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_ships(self):
        """ lives"""
        self.ships = Group()
        for next_ship in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.rect.x =15 + next_ship*ship.rect.width
            ship.rect.y =20
            self.ships.add(ship)

    def show_score(self):
        """show score on screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)
