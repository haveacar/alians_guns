import pygame
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    """main func"""
    pygame.init()
    # set up screen
    screen = pygame.display.set_mode((1000, 750))
    pygame.display.set_caption("Aliens guns")

    # set up background image
    background_image = pygame.image.load("images/background_image.jpg")
    background_image = pygame.transform.scale(background_image, (1000, 750))
    screen.blit(background_image, (0, 0))

    ship = Ship(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    score = Scores(screen, stats)

    # main loop
    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(background_image, screen, stats, score, ship, inos, bullets)
            controls.update_bullets(screen, stats, score, inos, bullets)
            controls.update_inos(stats, screen, score, ship, inos, bullets)


run()
