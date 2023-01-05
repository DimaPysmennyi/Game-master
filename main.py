import pygame
import modules.area as area
from modules.player import hero
import modules.settings as settings
import modules.enemy as enemy
from modules.npc import prisoner


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
            settings.button_start.blit_sprite(win)
            #mouse = pygame.mouse.get_pos()
            pressing = pygame.key.get_pressed()

            # if pygame.MOUSEBUTTONDOWN and :
            if pressing[pygame.K_SPACE]:
                settings.scene = "loc1"
            # if pygame.rect.collidepoint(settings.button):
            #     settings.scene = "loc1"
        
        if settings.scene == "loc1":
            
            pygame.mixer.music.load('sounds\\bg.mp3')
            pygame.mixer.music.play()

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
                turret.load_image(direction=True)
                turret.blit_sprite(win)
                enemy.turret.shoot(win, 200, width=80, height=25)
            
            for npc in area.list_npc:
                npc.load_image(direction=True)
                npc.blit_sprite(win)

            hero.move(area.list_block_area)
            hero.exit(area)
            hero.blit_sprite(win)
            hero.health_font(win)
            if hero.SHOW_DIALOG == True:
                prisoner.dialog("Вітаю! Зараз ти знаходишся у межгалактичній в'язниці.", win)
            
            if hero.HEALTH <= 0:
                hero.die(win)
                settings.scene = "game_over"

            

        if settings.scene == "game_over":
            win.fill((168, 0, 0))

            settings.button_restart.blit_sprite(win)

            pressing = pygame.key.get_pressed()
            if pressing[pygame.K_SPACE]:
                settings.scene = "loc1"


            # enemy.bullet1.draw(win)


            print(hero.HEALTH)

            
            # print(hero.GRAVITY)
            
        # hero.draw(win)
        

        clock.tick(60)
        pygame.display.flip()

run_game()