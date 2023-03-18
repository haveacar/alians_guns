import pygame

class Bullet(pygame.sprite.Sprite):
    """class bullet"""
    def __init__(self, screen, ship):
      super(Bullet, self).__init__()
      self.screen = screen
      self.rect = pygame.Rect(0, 0, 2, 12)
      self.color = 255, 255, 255
      self.speed = 4.5
      self.rect.centerx = ship.rect.centerx
      self.rect.top = ship.rect.top
      self.y = float(self.rect.y)

    def update(self):
        """update bullet"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)