import pygame

class Ship():
    def __init__(self, screen):
        """ship int"""

        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.mright = False
        self.mleft = False

    def output(self):
        """draw ship"""
        self.screen.blit(self.image, self.rect)


    def update_ship(self):
        """pos. ship"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2
        elif  self.mleft and self.rect.left > 0:
            self.center -= 2

        self.rect.centerx = self.center

    def create_ship(self):
        """create ship on center"""
        self.center = self.screen_rect.centerx