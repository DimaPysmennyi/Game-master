import pygame
import modules.area as area
from modules.player import hero


pygame.init()

win_width = 840
win_height = 840

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Game")

def run_game():

    game = True
    clock = pygame.time.Clock()    

    while game:
        win.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        
        for wall in area.list_block_area:
            wall.blit_sprite(win)
            # wall.draw(win)

        for door in area.list_door_right:
            # door.draw(win)
            door.blit_sprite(win)
        for door in area.list_door_left:
            # door.draw(win)
            door.blit_sprite(win)

        hero.move(area.list_block_area)
        hero.exit(area)
        # print(hero.GRAVITY)
        print(f"jump {hero.JUMP}")
        hero.blit_sprite(win)
        # hero.draw(win)
        

        clock.tick(60)
        pygame.display.flip()

run_game()