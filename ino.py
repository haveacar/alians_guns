import pygame

class Ino(pygame.sprite.Sprite):
    """class Ino(computer player)"""

    def __init__(self, screen):
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/al.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self):
        """draw enemy"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """moving enemy"""

        self.y += 0.2
        self.rect.y = self.y
