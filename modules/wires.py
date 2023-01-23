import pygame
import modules.settings as settings
import modules.buttons as btns

wires_list_left = []
wires_list_right = []
lights_on = False

def wires(win):
    global lights_on
    settings.wires.blit_sprite(win)
    btns.back_button.blit_sprite(win)
    lights_on = True
    if btns.back_button.button_pressing():
        settings.scene = "loc3" 

# :ratJAM: