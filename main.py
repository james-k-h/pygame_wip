import pygame
from utils.constants import *

pygame.init()
pygame.display.set_caption("Platformer")

window = pygame.display.set_mode((WIDTH, HEIGHT))

from objects.player import Player
from utils.helper_funcs import *
from objects.object import Object
from objects import *
from utils.background import *
from objects.trampoline import *


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Pink.png")

    block_size = 96

    player = Player(100, 100, 50, 50)
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    # trampoline = Trampoline(300, HEIGHT - block_size - 64, 16, 32)
    fire.on()
    # trampoline.on()
    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
  
    
    # add in blocks / objects
    objects = [*floor, Block(0, HEIGHT - block_size *2, block_size),
               Block(block_size * 3, HEIGHT - block_size * 4, block_size), Block(block_size * 4, HEIGHT - block_size * 4, block_size), 
               Block(block_size * 5, HEIGHT - block_size * 6, block_size), Block(block_size * 6, HEIGHT - block_size * 6, block_size),
               Block(block_size * 6, HEIGHT - block_size * 7, block_size),
               Block(block_size * 7, HEIGHT - block_size * 7, block_size), 
               fire]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2:
                    player.jump()

        player.loop(FPS)
        fire.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
