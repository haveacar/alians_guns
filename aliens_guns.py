import sys
import pygame
import controls
from ship import Ship
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import time
from database import *


def run(max_score, email_user, name_user):
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
    stats = Stats(max_score, email_user, name_user)
    score = Scores(screen, stats)

    # main loop
    while True:
        controls.events(screen, ship, bullets)
        if stats.run_game:
            ship.update_ship()
            controls.update(background_image, screen, stats, score, ship, inos, bullets)
            controls.update_bullets(screen, stats, score, inos, bullets)
            controls.update_inos(stats, screen, score, ship, inos, bullets)

        else:
            # game over
            game_over_image = pygame.image.load("images/game_over.jpg")
            screen.blit(game_over_image, (220, 200))
            pygame.display.update()
            stats.update_sql()
            time.sleep(3)
            sys.exit()


if __name__ == '__main__':
    login = Login()  # init object class login

    # check flag
    if login.flag_game:
        mx_score, mail, name = login.high_score()
        run(mx_score, mail, name)

