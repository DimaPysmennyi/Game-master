import pygame
import modules.player as player
import modules.settings as settings
import modules.buttons as btns

pygame.init()

button_list = []



mouse = pygame.mouse.get_pos()
mouse_pressed = pygame.mouse.get_pressed()

def vending_machine(win):
    for button in button_list:
        button.blit_sprite(win)
    
    if btns.button1.button_pressing() == True:
        player.hero.INVENTORY.append("screwdriver")



