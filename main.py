import pygame
import modules.area as area
from modules.player import hero
import modules.settings as settings
import modules.enemy as enemy
from modules.npc import prisoner, illya
import modules.jokes as jokes
import random

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
        print(settings.scene)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        if settings.scene == "menu":
            settings.bg_menu.blit_sprite(win)
            settings.button_start.blit_sprite(win)
            settings.button_exit.blit_sprite(win)
            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if mouse_pressed[0]:
                if mouse[0] >= settings.button_start.X and mouse[0] <= settings.button_start.X + settings.button_start.WIDTH:
                    if mouse[1] >= settings.button_start.Y and mouse[1] <= settings.button_start.Y + settings.button_start.HEIGHT:
                        settings.scene = "cutscene1"

                    if mouse[0] >= settings.button_exit.X and mouse[0] <= settings.button_exit.X + settings.button_exit.WIDTH:
                        if mouse[1] >= settings.button_exit.Y and mouse[1] <= settings.button_exit.Y + settings.button_exit.HEIGHT:
                            game = False
            # if pygame.MOUSEBUTTONDOWN and :
            # if pressing[pygame.K_SPACE]:
            #     settings.scene = "loc1"
            # if pygame.rect.collidepoint(settings.button):
            #     settings.scene = "loc1"
        if settings.scene == "cutscene1":
            
            if settings.cutscene_speed < 300:
                settings.cutscene.blit_sprite(win)
                settings.cutscene_speed += 1
                
            else:
                settings.scene = "loc1"

        if settings.scene == "loc1":
            win.fill((0, 0, 0))

            settings.bg1.blit_sprite(win)
            

            print(settings.laser.X, settings.laser.Y)
            

            for wall in area.list_block_area:
                wall.blit_sprite(win)
            
            for bed in area.list_bed:
                bed.blit_sprite(win)
                # wall.draw(win)

            for door in area.list_door_right:
                # door.draw(win)
                door.blit_sprite(win)
            for door in area.list_door_left:
                # door.draw(win)
                door.blit_sprite(win)
                
            
            for turret in area.list_turrets:
                turret.load_image()
                turret.blit_sprite(win)
                enemy.turret.shoot(win, "R", 200, width=80, height=25)

            
            for npc in area.list_npc:
                npc.load_image(direction=True)
                npc.blit_sprite(win)

            for object in area.list_lever:
                object.blit_sprite(win)
                

            for siren in area.list_siren:
                siren.blit_sprite(win)
                siren.enemy_move(area)

            print(hero.Y)
            hero.move(area.list_block_area, area.list_ladder)
            hero.show_dialog(prisoner)
            hero.exit(area)
            hero.blit_sprite(win)
            hero.health_font(win)
            
            if settings.trapdoor_pressed == True:
                settings.trapdoor.X = -100
                settings.trapdoor.RECT.x = -100
            
            if settings.laser_pressed == True:
                settings.laser.X = -100
                settings.laser.RECT.x = -100
                

            if prisoner.SHOW_DIALOG == True:
                prisoner.dialog(win, settings.player_head, settings.prisoner_head)
                if prisoner.SPEED_ANIMATION < 300:
                    prisoner.show_text("Вітаю! Зараз ти знаходишся у межгалактичній в'язниці. Тут,", win, 35, 55, 675)
                    prisoner.show_text("саме у космосі, за гратами знаходяться, ті хто здогадався", win, 35, 55, 705)
                    prisoner.show_text("про те, що на Землі існує тіньове правительство. Щоб", win, 35, 55, 735)
                    prisoner.show_text("втікти звідси, тобі доведеться знайти космічний корабель.", win, 35, 55, 765)
                    prisoner.SPEED_ANIMATION += 1
                
                if prisoner.SPEED_ANIMATION >= 300:
                    prisoner.show_text("Але обережно! Тут ти можеш зустріти різних", win, 35, 180, 675)
                    prisoner.show_text("небезпечних істот. Удачі!", win, 35, 280, 705)

            # print(settings.trapdoor.X, settings.trapdoor.Y)
            if hero.HEALTH == 0:
                settings.scene = "game_over"
        if settings.scene == "loc2":
            win.fill((0, 0, 0))

            settings.bg2.blit_sprite(win)

            for wall in area.list_block_area:
                wall.blit_sprite(win)
            
            for bed in area.list_bed:
                bed.blit_sprite(win)
                # wall.draw(win)

            for door in area.list_door_right:
                # door.draw(win)
                door.blit_sprite(win)
            for door in area.list_door_left:
                # door.draw(win)
                door.blit_sprite(win)
            
            for ladder in area.list_ladder:
                ladder.blit_sprite(win)
                
            
            for turret in area.list_turrets:
                turret.load_image()
                turret.blit_sprite(win)
                enemy.turret.shoot(win, "L", 200, width=80, height=25)

            
            for npc in area.list_npc:
                npc.load_image()
                npc.blit_sprite(win)
                

            for siren in area.list_siren:
                siren.blit_sprite(win)
                siren.enemy_move(area)

            print(hero.Y, illya.Y)
            hero.move(area.list_block_area, area.list_ladder)
            hero.show_dialog(illya)
            hero.exit(area)
            hero.blit_sprite(win)
            hero.health_font(win)
            
            if settings.trapdoor_pressed == True:
                settings.trapdoor.X = -100
                settings.trapdoor.RECT.x = -100
            
            if settings.laser_pressed == True:
                settings.laser.X = -100
                settings.laser.RECT.x = -100
                

            if illya.SHOW_DIALOG == True:
                if illya.JOKE == None:
                    illya.dialog(win, settings.player_head, settings.illya_head)
                    # if illya.SPEED_ANIMATION < 300:
                    illya.show_text("Здоров. Мене звати Ілля та я дуже серйозний трикутник.", win, 35, 55, 675)
                    illya.show_text("Але якщо забажаєш, я можу розповісти тобі один жарт.", win, 35, 55, 705)
                    illya.show_text("Хочеш?", win, 35, 55, 735)
                    settings.yes_button.blit_sprite(win)
                    settings.no_button.blit_sprite(win)
                    mouse = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:
                        if mouse[0] >= settings.yes_button.X and mouse[0] <= settings.yes_button.X + settings.yes_button.WIDTH:
                            if mouse[1] >= settings.yes_button.Y and mouse[1] <= settings.yes_button.Y + settings.yes_button.HEIGHT:
                                illya.JOKE = "tell"
                                index_joke = random.randint(0, 6)

                        if mouse[0] >= settings.no_button.X and mouse[0] <= settings.no_button.X + settings.no_button.WIDTH:
                            if mouse[1] >= settings.no_button.Y and mouse[1] <= settings.no_button.Y + settings.no_button.HEIGHT:
                                illya.JOKE = "refuse"

                if illya.JOKE == "tell":
                    illya.dialog(win, settings.player_head, settings.illya_head)

                    jokes.tell(index_joke, win)

                if illya.JOKE == "refuse":
                    illya.dialog(win, settings.player_head, settings.illya_head)
                    illya.show_text("Ну і будь ласка!", win, 35, 55, 675)
                    # illya.SPEED_ANIMATION += 1

                # if illya.SPEED_ANIMATION >= 300:
                #     illya.show_text("Але обережно! Тут ти можеш зустріти різних", win, 35, 180, 675)
                #     illya.show_text("небезпечних істот. Удачі!", win, 35, 280, 705)

            # print(settings.trapdoor.X, settings.trapdoor.Y)
            if hero.HEALTH == 0:
                settings.scene = "game_over"

        if settings.scene == "game_over":
            win.fill((168, 0, 0))
            # pygame.mixer.music.load("sounds\\bg.mp3")
            # pygame.mixer.music.play(-1)
            settings.bg_death.blit_sprite(win)

            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            settings.button_restart.blit_sprite(win)
            if mouse_pressed[0]:
                if mouse[0] >= settings.button_restart.X and mouse[0] <= settings.button_restart.X + settings.button_restart.WIDTH:
                    if mouse[1] >= settings.button_restart.Y and mouse[1] <= settings.button_restart.Y + settings.button_restart.HEIGHT:
                        hero.HEALTH = 3
                        hero.X = 120
                        hero.Y = 184
                        hero.RECT.x = 120
                        hero.RECT.y = 184
                        settings.trapdoor.X = 540
                        settings.trapdoor.Y = 240
                        settings.trapdoor.RECT.x = 540
                        settings.trapdoor.RECT.y = 240
                        settings.lever.NAME_IMG = "images\lever_off.png"
                        settings.laser.X = 60
                        settings.laser.Y = 480
                        settings.laser.RECT.x = 60
                        settings.laser.RECT.y = 480
                        prisoner.SPEED_ANIMATION = 0
                        for ladder in area.list_ladder:
                            ladder.blit_sprite(win)
                        settings.trapdoor_pressed = False
                        settings.laser_pressed = False
                        settings.lever.blit_sprite(win)
                        settings.lever2.blit_sprite(win)
                        hero.CURRENT_LEVEL = 0
                        settings.scene = "loc1"



            # enemy.bullet1.draw(win)

            
            # print(hero.GRAVITY)
            
        # hero.draw(win)
        

        clock.tick(60)
        pygame.display.flip()

run_game()