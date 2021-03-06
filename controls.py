import pygame
import sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #right
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
                #right
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                ship.mleft = False


def update(bg_color, screen, stats, ship, inos, bullets):
    #Screen load
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, inos, bullets):
    #delete bullets
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)

    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def ship_kill(stats, screen, ship, inos, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, ship, inos, bullets):
    #moving enemy
    inos.update()
    if pygame.sprite.spritecollideany(ship, inos):
        ship_kill(stats, screen, ship, inos, bullets)
    inos_check(stats, screen, ship, inos, bullets)

def inos_check(stats, screen, ship, inos, bullets):
    #check or army inos in the down screen
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, ship, inos, bullets)
            break

def create_army(screen, inos):
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
