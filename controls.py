import pygame
import sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, ship, bullets):
    """events func"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # keydown
            # right move ship
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            # left move ship
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:  # keyup
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update(background_image, screen, stats, score, ship, inos, bullets):
    """"Screen load"""
    screen.blit(background_image, (0, 0))
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, score, inos, bullets):
    """delete bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    # check collision's dictionary for stats
    if collisions:
        for inos in collisions.values():
            stats.score += 15 * len(inos)
        score.image_score()
        check_high_score(stats, score)
        score.image_ships()

    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def ship_kill(stats, screen, score, ship, inos, bullets):
    """contact ship and inos"""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        score.image_ships()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False



def update_inos(stats, screen, score, ship, inos, bullets):
    """moving enemy"""
    inos.update()
    if pygame.sprite.spritecollideany(ship, inos):
        ship_kill(stats, screen,score, ship, inos, bullets)
    inos_check(stats, screen, score, ship, inos, bullets)


def inos_check(stats, screen,score,  ship, inos, bullets):
    """check or army inos in the down screen"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, score, ship, inos, bullets)
            break


def create_army(screen, inos):
    """create enemy's objects"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((1000 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((1000 - 500 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)


def check_high_score(stats, sc):
    """check high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
