import pygame
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores


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
    score= Scores(screen, stats)

    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(bg_color, screen, stats, score, ship, inos, bullets)
            controls.update_bullets(screen, stats, score, inos, bullets)
            controls.update_inos(stats, screen, ship, inos, bullets)



run()