import pygame
import modules.player as player
import modules.settings as settings
import modules.buttons as btns

pygame.init()

show_screwdriver = True
mouse = pygame.mouse.get_pos()
mouse_pressed = pygame.mouse.get_pressed()

def vending_machine(win):
    global show_screwdriver
    if btns.button5.button_pressing() == True:
        show_screwdriver = False
        player.hero.INVENTORY.append("screwdriver")
        settings.vending_machine_inside.blit_sprite(win)
    
    else:
        settings.vending_machine_inside.blit_sprite(win)
        if show_screwdriver == True:
            settings.screwdriver.blit_sprite(win)



