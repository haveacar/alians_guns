import pygame
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats


def run():
    """main func"""
    pygame.init()
    screen = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption("Aliens guns")
    bg_color = (75, 127, 173)
    ship = Ship(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()

    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(bg_color, screen, stats, ship, inos, bullets)
            controls.update_bullets(screen, inos, bullets)
            controls.update_inos(stats, screen, ship, inos, bullets)



run()