import pygame
from modules.area import list_create_area, hero


pygame.init()

win_width = 800
win_height = 800





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
        
        for wall in list_create_area:
            wall.draw(win)

        hero.move(list_create_area)
        # hero.blit_sprite(win)
        hero.draw(win)
        

        clock.tick(60)
        pygame.display.flip()

   

run_game()