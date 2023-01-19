import pygame
import modules.area as area
from modules.player import hero
import modules.settings as settings
import modules.enemy as enemy
from modules.npc import prisoner, illya, security_guy
import modules.vending_machine as mvm
import modules.jokes as jokes
import modules.dialogs as dialogs
import random

pygame.init()

win_width = 840
win_height = 840
srez = 0


win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Game")

def run_game():
    game = True
    clock = pygame.time.Clock()    
    refuse_srez = 0
    refuse_str = "Ну і будь ласка!"

    while game:
        win.fill((0,0,0))
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

            hero.move(area.list_block_area)
            hero.show_dialog(prisoner)
            hero.exit(area, enemy, win)
            hero.blit_sprite(win)
            hero.health_font(win)
            
            if settings.trapdoor_pressed == True:
                for trapdoor in area.list_trapdoor:
                    trapdoor.X = -100
                    trapdoor.RECT.x = -100
            
            if settings.laser_pressed == True:
                settings.laser.X = -100
                settings.laser.RECT.x = -100
                

            if prisoner.SHOW_DIALOG == True:
                prisoner.dialog(win, settings.player_head, settings.prisoner_head)
                if prisoner.CURRENT_STR >= 0:
                    dialogs.prisoner_dialog[0][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[0][0][0:dialogs.prisoner_dialog[0][1]], win, 35, 55, 675)
                if prisoner.CURRENT_STR >= 1:
                    dialogs.prisoner_dialog[1][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[1][0][0:dialogs.prisoner_dialog[1][1]], win, 35, 55, 705)
                if prisoner.CURRENT_STR >= 2:
                    dialogs.prisoner_dialog[2][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[2][0][0:dialogs.prisoner_dialog[2][1]], win, 35, 55, 735)
                if prisoner.CURRENT_STR >= 3:
                    dialogs.prisoner_dialog[3][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[3][0][0:dialogs.prisoner_dialog[3][1]], win, 35, 55, 765)   

                if dialogs.prisoner_dialog[0][1] > len(dialogs.prisoner_dialog[0][0]):
                    # prisoner.DIALOG_Y += 30
                    if prisoner.CURRENT_STR < 1: 
                        prisoner.CURRENT_STR += 1
                if dialogs.prisoner_dialog[1][1] > len(dialogs.prisoner_dialog[1][0]):
                    # prisoner.DIALOG_Y += 30
                    if prisoner.CURRENT_STR < 2: 
                        prisoner.CURRENT_STR += 1
                if dialogs.prisoner_dialog[2][1] > len(dialogs.prisoner_dialog[2][0]):
                    # prisoner.DIALOG_Y += 30
                    if prisoner.CURRENT_STR < 3: 
                        prisoner.CURRENT_STR += 1

                if dialogs.prisoner_dialog[3][1] > len(dialogs.prisoner_dialog[3][0]):
                    # prisoner.DIALOG_Y += 30
                    if prisoner.CURRENT_STR < 4: 
                        prisoner.CURRENT_STR += 1   

                # if prisoner.CURRENT_STR > 4:
                    # prisoner.CURRENT_STR = 4

                # prisoner.show_text("втікти звідси, тобі доведеться знайти космічний корабель.", win, 35, 55, 765)
                
                # if prisoner.SPEED_ANIMATION >= 300:
                #     prisoner.show_text("Але обережно! Тут ти можеш зустріти різних", win, 35, 180, 675)
                #     prisoner.show_text("небезпечних істот. Удачі!", win, 35, 280, 705)

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
                turret.load_image(direction=True)
                turret.blit_sprite(win)
                enemy.turret.shoot(win, "L", 200, width=80, height=25)

            
            for npc in area.list_npc:
                npc.load_image()
                npc.blit_sprite(win)
                
            for object in area.list_lever:
                object.blit_sprite(win)

            for siren in area.list_siren:
                siren.blit_sprite(win)
                siren.enemy_move(area)


            print(hero.INVENTORY)
            if not "keys" in hero.INVENTORY:
                settings.keys.blit_sprite(win)

            hero.move(area.list_block_area)
            hero.show_dialog(illya)
            hero.exit(area, enemy, win)
            hero.blit_sprite(win)
            hero.health_font(win)
            
            # if settings.trapdoor2_pressed == True:
            for trapdoor in area.list_trapdoor:
                trapdoor.blit_sprite(win)
        

                

            if illya.SHOW_DIALOG == True:
                if illya.JOKE == None:
                    illya.dialog(win, settings.player_head, settings.illya_head)
                    # if illya.SPEED_ANIMATION < 300:
                    if illya.CURRENT_STR >= 0:
                        dialogs.illya_dialog[0][1] += 1
                        illya.show_text(dialogs.illya_dialog[0][0][0:dialogs.illya_dialog[0][1]], win, 35, 55, 675)
                    if illya.CURRENT_STR >= 1:
                        dialogs.illya_dialog[1][1] += 1
                        illya.show_text(dialogs.illya_dialog[1][0][0:dialogs.illya_dialog[1][1]], win, 35, 55, 705)
                    if illya.CURRENT_STR >= 2:
                        dialogs.illya_dialog[2][1] += 1
                        illya.show_text(dialogs.illya_dialog[2][0][0:dialogs.illya_dialog[2][1]], win, 35, 55, 735)  
                        settings.yes_button.blit_sprite(win)
                        settings.no_button.blit_sprite(win) 

                    if dialogs.illya_dialog[0][1] > len(dialogs.illya_dialog[0][0]):
                        # prisoner.DIALOG_Y += 30
                        if illya.CURRENT_STR < 1: 
                            illya.CURRENT_STR += 1
                    if dialogs.illya_dialog[1][1] > len(dialogs.illya_dialog[1][0]):
                        # prisoner.DIALOG_Y += 30
                        if illya.CURRENT_STR < 2: 
                            illya.CURRENT_STR += 1
                    if dialogs.illya_dialog[2][1] > len(dialogs.illya_dialog[2][0]):
                        # prisoner.DIALOG_Y += 30
                        if illya.CURRENT_STR < 3: 
                            illya.CURRENT_STR += 1

                        
                    mouse = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()

                    if mouse_pressed[0]:
                        if mouse[0] >= settings.yes_button.X and mouse[0] <= settings.yes_button.X + settings.yes_button.WIDTH:
                            if mouse[1] >= settings.yes_button.Y and mouse[1] <= settings.yes_button.Y + settings.yes_button.HEIGHT:
                                illya.JOKE = "tell"
                                index_joke = random.randint(0, 5)

                        if mouse[0] >= settings.no_button.X and mouse[0] <= settings.no_button.X + settings.no_button.WIDTH:
                            if mouse[1] >= settings.no_button.Y and mouse[1] <= settings.no_button.Y + settings.no_button.HEIGHT:
                                illya.JOKE = "refuse"

                if illya.JOKE == "tell":
                    illya.dialog(win, settings.player_head, settings.illya_head)

                    jokes.tell(index_joke, win)

                if illya.JOKE == "refuse":
                    illya.dialog(win, settings.player_head, settings.illya_head)
                    
                    if illya.CURRENT_STR >= 3:
                        refuse_srez += 1
                        illya.show_text(refuse_str[0:refuse_srez], win, 35, 55, 675)
                    # illya.SPEED_ANIMATION += 1

            if hero.HEALTH == 0:
                settings.scene = "game_over"

        if settings.scene == "loc3":
            win.fill((0, 0, 0))
            for block in area.list_block_area:
                block.blit_sprite(win)

            for door in area.list_door_right:
                # door.draw(win)
                door.blit_sprite(win)

            for door in area.list_door_left:
                # door.draw(win)
                door.blit_sprite(win)

            for npc in area.list_npc:
                npc.blit_sprite(win)

            for vm in area.list_vending_machine:
                vm.blit_sprite(win)

            hero.move(area.list_block_area)
            hero.show_dialog(security_guy)
            hero.exit(area, enemy, win)
            hero.blit_sprite(win)
            hero.health_font(win)

            if security_guy.SHOW_DIALOG == True:
                security_guy.dialog(win, settings.player_head, settings.security_guy_head)
                if settings.vending_machine_pressed == False:
                    if security_guy.CURRENT_STR >= 0:
                        dialogs.security_guy_dialog[0][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[0][0][0:dialogs.security_guy_dialog[0][1]], win, 35, 55, 675)
                    if security_guy.CURRENT_STR >= 1:
                        dialogs.security_guy_dialog[1][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[1][0][0:dialogs.security_guy_dialog[1][1]], win, 35, 55, 705)
                    if security_guy.CURRENT_STR >= 2:
                        dialogs.security_guy_dialog[2][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[2][0][0:dialogs.security_guy_dialog[2][1]], win, 35, 55, 735)  

                    if dialogs.security_guy_dialog[0][1] > len(dialogs.security_guy_dialog[0][0]):
                        # prisoner.DIALOG_Y += 30
                        if security_guy.CURRENT_STR < 1: 
                            security_guy.CURRENT_STR += 1
                    if dialogs.security_guy_dialog[1][1] > len(dialogs.security_guy_dialog[1][0]):
                        # prisoner.DIALOG_Y += 30
                        if security_guy.CURRENT_STR < 2: 
                            security_guy.CURRENT_STR += 1
                    if dialogs.security_guy_dialog[2][1] > len(dialogs.security_guy_dialog[2][0]):
                        # prisoner.DIALOG_Y += 30
                        if security_guy.CURRENT_STR < 3: 
                            security_guy.CURRENT_STR += 1


                # security_guy.show_text("Лише з нею ти зможеш увімкнути ліфт. Я знаю, що вона є в", win, 35, 55, 705)
                # security_guy.show_text("цьому автоматі, зверху від мене.", win, 35, 55, 735)

                if settings.vending_machine_pressed == True:
                    security_guy.dialog(win, settings.player_head, settings.security_guy_head)
                    if not "keys" in hero.INVENTORY:
                        if settings.vending_machine_pressed == False:
                            srez = 0
                            for symbol in range(len(dialogs.security_guy_dialog[3])):
                                srez += 1
                                security_guy.show_text(dialogs.security_guy_dialog[3][0:srez], win, 35, 55, 675)
                                if symbol == dialogs.security_guy_dialog[3][-1]:
                                    srez = 0

                            for symbol in range(len(dialogs.security_guy_dialog[4])):
                                srez += 1
                                security_guy.show_text(dialogs.security_guy_dialog[4][0:srez], win, 35, 55, 705)
                                if symbol == dialogs.security_guy_dialog[4][-1]:
                                    srez = 0

                            for symbol in range(len(dialogs.security_guy_dialog[5])):
                                srez += 1
                                security_guy.show_text(dialogs.security_guy_dialog[5][0:srez], win, 35, 55, 735)
                                if symbol == dialogs.security_guy_dialog[5][-1]:
                                    srez = 0

                    if "keys" in hero.INVENTORY:
                        hero.INVENTORY.remove("keys")
                        srez = 0
                        for symbol in range(len(dialogs.security_guy_dialog[6])):
                            srez += 1
                            security_guy.show_text(dialogs.security_guy_dialog[6][0:srez], win, 35, 55, 735)
                            if symbol == dialogs.security_guy_dialog[6][-1]:
                                srez = 0
                        hero.INVENTORY.append("coin")
        
        if settings.scene == "vending machine":
            settings.back_button.blit_sprite(win)
            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed[0]:
                if mouse[0] >= settings.back_button.X and mouse[0] <= settings.back_button.X + settings.back_button.WIDTH:
                    if mouse[1] >= settings.back_button.Y and mouse[1] <= settings.back_button.Y + settings.back_button.HEIGHT:
                        settings.scene = "loc3"

            if "coin" in hero.INVENTORY:
                mvm.vending_machine(win)
            else:
                font = pygame.font.SysFont('fonts\Digital_Thin.ttf', 40)
                text1 = font.render(str("Необхідно внести монету!"), 1, (255,255,255), (215,0,0))
                win.blit(text1, (200, 420))


        if settings.scene == "game_over":
            win.fill((168, 0, 0))
            # pygame.mixer.music.load("sounds\\bg.mp3")
            # pygame.mixer.music.play(-1)
            settings.bg_death.blit_sprite(win)

            mouse = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            settings.button.blit_sprite(win)
            if mouse_pressed[0]:
                if mouse[0] >= settings.button.X and mouse[0] <= settings.button.X + settings.button.WIDTH:
                    if mouse[1] >= settings.button.Y and mouse[1] <= settings.button.Y + settings.button.HEIGHT:
                        hero.HEALTH = 3
                        hero.X = 120
                        hero.Y = 184
                        hero.RECT.x = 120
                        hero.RECT.y = 184
                        settings.bg1.blit_sprite(win)
                        for trapdoor in area.list_trapdoor:
                            trapdoor.X = 540
                            trapdoor.Y = 240
                            trapdoor.RECT.x = 540
                            trapdoor.RECT.y = 240
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