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
import modules.buttons as btns
import modules.minigame1 as minigame1
import modules.wires as wires
import modules.terminal as terminal
import modules.sound as sound

pygame.init()

win_width = 840
win_height = 840
srez = 0


win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Illuminati Confirmed")

def run_game():

    game = True
    clock = pygame.time.Clock()    
    refuse_srez = 0
    refuse_str = "Ну і будь ласка!" #x = 12, 120. y = 160, height = 50, width = 110

    while game:
        print(hero.Y, "герой")
        print(settings.medkit.Y, "откуда готовилось нападение")
        sound.sound_repeat += 1 
        if settings.sound == True:
            sound.bg_music("audio.wav")
        win.fill((0,0,0))
        # print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
        if settings.scene == "menu":
            settings.bg_menu.blit_sprite(win)
            btns.button_start.blit_sprite(win)
            btns.button_exit.blit_sprite(win)
            btns.sound_switch.blit_sprite(win)

            if btns.button_start.button_pressing() == True:
                settings.scene = "cutscene1"
                

            if btns.button_exit.button_pressing() == True:
                game = False

            if btns.sound_switch.button_pressing():
                if sound.sound_repeat % 7 == 0:
                    sound.sound("button.wav", 1)
                    if settings.sound == True:
                        btns.sound_switch.NAME_IMG = "images\sound_on.png"
                        btns.sound_switch.load_image()
                        settings.sound = False
                    else:
                        btns.sound_switch.NAME_IMG = "images\sound_off.png"
                        btns.sound_switch.load_image()
                        settings.sound = True
        
        if settings.scene == "cutscene1":
            # print(settings.cutscene_speed)
            
            if settings.cutscene_speed < 300:
                settings.cutscene_speed += 1

            if settings.cutscene_speed > 299 and settings.cutscene_speed < 600:
                settings.cutscene.NAME_IMG = "images\cutscene1_5.png"
                settings.cutscene.load_image()
                settings.cutscene_speed += 1
            
            if settings.cutscene_speed > 599:
                if settings.cutscene1_speed == 20:
                    settings.current_frame1 += 1
                    settings.cutscene.NAME_IMG = f"images\\cutscene1\\{str(settings.current_frame1)}.png"
                    settings.cutscene.load_image()
                    settings.cutscene1_speed = 0
                if settings.current_frame1 >= 25:
                    settings.scene = "loc1"
                else:
                    settings.cutscene1_speed += 1
            settings.cutscene.blit_sprite(win)



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
                enemy.turret.shoot(win, "R", 200)

            
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
                    prisoner.show_text(dialogs.prisoner_dialog[0][0][0:dialogs.prisoner_dialog[0][1]], win, 22, 55, 675)
                if prisoner.CURRENT_STR >= 1:
                    dialogs.prisoner_dialog[1][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[1][0][0:dialogs.prisoner_dialog[1][1]], win, 22, 55, 705)
                if prisoner.CURRENT_STR >= 2:
                    dialogs.prisoner_dialog[2][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[2][0][0:dialogs.prisoner_dialog[2][1]], win, 22, 55, 735)
                if prisoner.CURRENT_STR >= 3:
                    dialogs.prisoner_dialog[3][1] += 1
                    prisoner.show_text(dialogs.prisoner_dialog[3][0][0:dialogs.prisoner_dialog[3][1]], win, 22, 55, 765)   

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

            for medkit in area.list_medkit:
                medkit.blit_sprite(win)
            
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
                enemy.turret.shoot(win, "L", 200)

            
            for npc in area.list_npc:
                npc.load_image()
                npc.blit_sprite(win)
                
            for object in area.list_lever:
                object.blit_sprite(win)

            for siren in area.list_siren:
                siren.blit_sprite(win)
                siren.enemy_move(area)



            # print(hero.INVENTORY)
            if settings.need_keys == True:
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
                        illya.show_text(dialogs.illya_dialog[0][0][0:dialogs.illya_dialog[0][1]], win, 22, 55, 675)
                    if illya.CURRENT_STR >= 1:
                        dialogs.illya_dialog[1][1] += 1
                        illya.show_text(dialogs.illya_dialog[1][0][0:dialogs.illya_dialog[1][1]], win, 22, 55, 705)
                    if illya.CURRENT_STR >= 2:
                        dialogs.illya_dialog[2][1] += 1
                        illya.show_text(dialogs.illya_dialog[2][0][0:dialogs.illya_dialog[2][1]], win, 22, 55, 735)  
                        btns.no_button.blit_sprite(win)
                        btns.yes_button.blit_sprite(win) 

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

                        
                        if btns.yes_button.button_pressing() == True:
                            illya.JOKE = "tell"
                            index_joke = random.randint(0, 4)

                        if btns.no_button.button_pressing() == True:
                            illya.JOKE = "refuse"

                if illya.JOKE == "tell":
                    illya.dialog(win, settings.player_head, settings.illya_head)

                    jokes.tell(index_joke, win)

                if illya.JOKE == "refuse":
                    illya.dialog(win, settings.player_head, settings.illya_head)
                    
                    if illya.CURRENT_STR >= 3:
                        refuse_srez += 1
                        illya.show_text(refuse_str[0:refuse_srez], win, 22, 55, 675)
                    # illya.SPEED_ANIMATION += 1

            if hero.HEALTH == 0:
                settings.scene = "game_over"

        if settings.scene == "loc3":

            if settings.password[0] == settings.password[1] or settings.password[0] == settings.password[2] or settings.password[0] == settings.password[3]:
                settings.password = str(random.randint(1000, 10000))
            if settings.password[1] == settings.password[2] or settings.password[1] == settings.password[3]:
                settings.password = str(random.randint(1000, 10000))
            if settings.password[2] == settings.password[3]:
                settings.password = str(random.randint(1000, 10000))

            win.fill((0, 0, 0))
            settings.bg3.blit_sprite(win)
            for block in area.list_block_area:
                block.blit_sprite(win)

            for medkit in area.list_medkit:
                medkit.blit_sprite(win)
            
            for shkaf in area.list_shkaf:
                # door.draw(win)
                shkaf.blit_sprite(win)

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
            
            for computer in area.list_computer:
                computer.blit_sprite(win)

            for balloon in area.list_balloon:
                balloon.blit_sprite(win)
            
            for ladder in area.list_ladder:
                ladder.blit_sprite(win)

            hero.move(area.list_block_area)
            hero.show_dialog(security_guy)
            hero.exit(area, enemy, win)
            settings.elec.blit_sprite(win)
            hero.blit_sprite(win)
            hero.health_font(win)
            

            if security_guy.SHOW_DIALOG == True:
                # print(security_guy.CURRENT_STR)
                security_guy.dialog(win, settings.player_head, settings.security_guy_head)
                # print(security_guy.CURRENT_STR)
                if settings.vending_machine_pressed == False:
                    settings.need_vending_machine = True
                    if security_guy.CURRENT_STR >= 0:
                        dialogs.security_guy_dialog[0][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[0][0][0:dialogs.security_guy_dialog[0][1]], win, 22, 55, 675)
                    if security_guy.CURRENT_STR >= 1:
                        dialogs.security_guy_dialog[1][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[1][0][0:dialogs.security_guy_dialog[1][1]], win, 22, 55, 705)
                    if security_guy.CURRENT_STR >= 2:
                        dialogs.security_guy_dialog[2][1] += 1
                        security_guy.show_text(dialogs.security_guy_dialog[2][0][0:dialogs.security_guy_dialog[2][1]], win, 22, 55, 735)  

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
                        settings.need_keys = True
                        if security_guy.CURRENT_STR >= 0:
                            dialogs.security_guy_dialog[3][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[3][0][0:dialogs.security_guy_dialog[3][1]], win, 22, 55, 675)
                        if security_guy.CURRENT_STR >= 1:
                            dialogs.security_guy_dialog[4][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[4][0][0:dialogs.security_guy_dialog[4][1]], win, 22, 55, 705)
                        if security_guy.CURRENT_STR >= 2:
                            dialogs.security_guy_dialog[5][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[5][0][0:dialogs.security_guy_dialog[5][1]], win, 22, 55, 735)  
                        if dialogs.security_guy_dialog[3][1] > len(dialogs.security_guy_dialog[3][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 1: 
                                security_guy.CURRENT_STR += 1
                        if dialogs.security_guy_dialog[4][1] > len(dialogs.security_guy_dialog[4][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 2: 
                                security_guy.CURRENT_STR += 1
                        if dialogs.security_guy_dialog[5][1] > len(dialogs.security_guy_dialog[5][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 3: 
                                security_guy.CURRENT_STR += 1

                    if "keys" in hero.INVENTORY:
                        if security_guy.CURRENT_STR >= 0:
                            dialogs.security_guy_dialog[6][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[6][0][0:dialogs.security_guy_dialog[6][1]], win, 22, 55, 675)  
                            if not "coin" in hero.INVENTORY:        
                                hero.INVENTORY.append("coin")
                        if security_guy.CURRENT_STR >= 1:
                            dialogs.security_guy_dialog[7][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[7][0][0:dialogs.security_guy_dialog[7][1]], win, 22, 55, 705)  
                        if security_guy.CURRENT_STR >= 2:
                            dialogs.security_guy_dialog[8][1] += 1
                            security_guy.show_text(dialogs.security_guy_dialog[8][0][0:dialogs.security_guy_dialog[8][1]], win, 22, 55, 735)  
                            
                        if dialogs.security_guy_dialog[6][1] > len(dialogs.security_guy_dialog[6][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 1: 
                                security_guy.CURRENT_STR += 1
                        if dialogs.security_guy_dialog[7][1] > len(dialogs.security_guy_dialog[7][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 2: 
                                security_guy.CURRENT_STR += 1
                        if dialogs.security_guy_dialog[8][1] > len(dialogs.security_guy_dialog[8][0]):
                            # prisoner.DIALOG_Y += 30
                            if security_guy.CURRENT_STR < 3: 
                                security_guy.CURRENT_STR += 1

            if security_guy.SHOW_DIALOG == False:
                security_guy.CURRENT_STR = 0

        if settings.scene == "wires":
            wires.wires(win)

        if settings.scene == "vending machine":
            
            if btns.back_button.button_pressing() == True:
                settings.scene = "loc3"

            if "coin" in hero.INVENTORY:
                mvm.vending_machine(win)
                for button in btns.button_list:
                    button.blit_sprite(win)
            else:
                font = pygame.font.Font('fonts\PixelFont.ttf', 20)
                text1 = font.render(str("Необхідно внести монету!"), 1, (255,255,255), (215,0,0))
                win.blit(text1, (250, 420))
            
            btns.back_button.blit_sprite(win)

        
        if settings.scene == "computer":
            if wires.lights_on == True:
                settings.win98.blit_sprite(win)
                btns.button_minigame1.blit_sprite(win)
                if btns.button_minigame1.button_pressing() == True:
                    settings.scene = "minigame1"
            if wires.lights_on == False:
                font = pygame.font.Font("fonts\PixelFont.ttf", 20)
                text1 = font.render(str("Необхідно увімкнути світло!"), 1, (255,255,255), (215,0,0))
                win.blit(text1, (250, 420)) 
            btns.back_button.blit_sprite(win)
            if btns.back_button.button_pressing():
                settings.scene = "loc3" 
            

        if settings.scene == "minigame1":
            minigame1.minigame1(win)
            font = pygame.font.Font('fonts\\PixelFont.ttf', 100)
            text = font.render("?+?=15", 1, (0,0,0), None)
            win.blit(text, (300, 150))
        
        if settings.scene == "terminal":
            terminal.terminal(win)
            btns.back_button.blit_sprite(win)
            if btns.back_button.button_pressing():
                area.list_block_area.clear()
                area.list_door_right.clear()
                area.list_door_left.clear()
                # area.list_door_left_rect.clear()
                area.list_turrets.clear()
                # area.list_turrets_rect.clear()
                area.list_bullet.clear()
                area.list_lever.clear()
                area.list_ladder.clear()
                area.list_bed.clear()
                area.list_npc.clear()
                area.list_siren.clear()
                area.list_vending_machine.clear()
                area.list_computer.clear()
                area.list_balloon.clear()
                area.list_shkaf.clear()
                terminal.input_list.clear()
                terminal.p0 = False
                terminal.p1 = False
                terminal.p2 = False
                terminal.p3 = False
                terminal.p4 = False
                terminal.p5 = False
                terminal.p6 = False
                terminal.p7 = False
                terminal.p8 = False
                terminal.p9 = False

                hero.CURRENT_LEVEL -= 1

                settings.scene = "loc3"
                area.create_area(600,120)


        if settings.scene == "loc4":
            settings.bg4.blit_sprite(win)
            settings.spaceship.blit_sprite(win)
            for block in area.list_block_area:
                block.blit_sprite(win)
            
            for door in area.list_door_left:
                door.blit_sprite(win)
            
            hero.move(area.list_block_area)
            hero.blit_sprite(win)
            hero.exit(area, enemy, win)
            hero.health_font(win)


        if settings.scene == "cutscene2":
            if settings.cutscene2_speed == 20:
                settings.current_frame2 += 1
                settings.cutscene2.NAME_IMG = f"images\\cutscene2\\{str(settings.current_frame2)}.png"
                settings.cutscene2.load_image()
                settings.cutscene2_speed = 0
            if settings.current_frame2 >= 25:
                settings.scene = "cutscene3"
            else:
                settings.cutscene2_speed += 1
            settings.cutscene2.blit_sprite(win)

        if settings.scene == "cutscene3":
            if settings.cutscene3_speed == 20:
                settings.current_frame3 += 1
                settings.cutscene3.NAME_IMG = f"images\\cutscene3\\{str(settings.current_frame3)}.png"
                settings.cutscene3.load_image()
                settings.cutscene3_speed = 0
            if settings.current_frame3 >= 7:
                settings.scene = "credits"
            else:
                settings.cutscene3_speed += 1
            settings.cutscene3.blit_sprite(win)
        
        if settings.scene == "credits":
            settings.credits.blit_sprite(win)

        if settings.scene == "game_over":
            win.fill((168, 0, 0))
            # pygame.mixer.music.load("sounds\\bg.mp3")
            # pygame.mixer.music.play(-1)
            settings.bg_death.blit_sprite(win)

        clock.tick(60)
        pygame.display.flip()

run_game()