import pygame
import modules.area as area
from modules.player import hero
import modules.settings as settings
import modules.enemy as enemy


pygame.init()

win_width = 840
win_height = 840

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Game")

def run_game():

    game = True
    clock = pygame.time.Clock()    

    while game:
        win.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        if settings.scene == "menu":
            win.fill((65,105,225))
            settings.button.blit_sprite(win)
            pressing = pygame.key.get_pressed()
            if pressing[pygame.K_SPACE]:
                settings.scene = "loc1"
            # if pygame.rect.collidepoint(settings.button):
            #     settings.scene = "loc1"
        
        if settings.scene == "loc1":
            
            for wall in area.list_block_area:
                wall.blit_sprite(win)
                # wall.draw(win)

            for door in area.list_door_right:
                # door.draw(win)
                door.blit_sprite(win)
            for door in area.list_door_left:
                # door.draw(win)
                door.blit_sprite(win)
            
            for turret in area.list_turrets:
                turret.draw(win)
                enemy.bullet.draw(win)
            

            hero.move(area.list_block_area)
            hero.exit(area)

            enemy.bullet.bullet_move()
            # print(hero.GRAVITY)
            hero.blit_sprite(win)
        # hero.draw(win)
        

        clock.tick(60)
        pygame.display.flip()

run_game()