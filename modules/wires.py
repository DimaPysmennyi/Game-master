import pygame
import modules.settings as settings
import modules.buttons as btns

wires_list_left = []
wires_list_right = []
left_pressed = False
right_pressed = False
lgw = False
lrw = False
lbw = False
lpw = False
lyw = False
rbw = False
rgw = False
rrw = False
ryw = False
rpw = False
lights_on = False

def wires(win):
    global lights_on
    global left_pressed
    global right_pressed
    global lgw
    global lrw
    global lbw
    global lpw
    global lyw
    global rbw
    global rgw
    global rrw
    global ryw
    global rpw
    settings.wires.blit_sprite(win)
    btns.back_button.blit_sprite(win)
    for wl in wires_list_left:
        if left_pressed == False:
            if wl.button_pressing():
                if wl == left_green_wire:
                    lgw = True
                if wl == left_red_wire:
                    lrw = True
                if wl == left_blue_wire:
                    lbw = True
                if wl == left_purple_wire:
                    lpw = True
                if wl == left_yellow_wire:
                    lyw = True

                left_pressed = True
                right_pressed = False
    
    for wr in wires_list_right:
        if left_pressed == True:
            # print('tuda1')
            if right_pressed == False:
                # print('tuda2')
                if wr.button_pressing():
                    # print("tuda3")
                    if wr == right_blue_wire:
                        rbw = True
                        if lbw == False:
                            rbw = False
                    if wr == right_red_wire:
                        rrw = True
                        if lrw == False:
                            rrw = False
                    if wr == right_purple_wire:
                        rpw = True
                        if lpw == False:
                            rpw = False
                    if wr == right_yellow_wire:
                        ryw = True
                        if lyw == False:
                            ryw = False
                    if wr == right_green_wire:
                        rgw = True
                        if lgw == False:
                            rgw = False

                    right_pressed = True
                    left_pressed = False
             
    if rbw == True and lbw == True:
        pygame.draw.line(win, (40,53,147), (120, 455), (720, 185), 20)
    
    if lgw == True and rgw == True:
        pygame.draw.line(win, (10,142,8), (120, 185), (720, 585), 20)
    
    if lpw == True and rpw == True:
        pygame.draw.line(win, (142,36,170), (120, 585), (720, 455), 20)
    
    if lrw == True and rrw == True:
        pygame.draw.line(win, (221,25,29), (120, 315), (720, 315), 20)
    
    if lyw == True and ryw == True:
        pygame.draw.line(win, (255,235,59), (120, 725), (720, 725), 20)
        
    
    if rbw == True and lbw == True and lgw == True and rgw == True and lrw == True and rrw == True and lpw == True and rpw == True and lyw == True and ryw == True:
        lights_on = True
    if btns.back_button.button_pressing():
        settings.scene = "loc3" 

# :ratJAM:

#x = 12, 120. y = 160, height = 50, width = 110

left_green_wire = btns.Button(
    width = 110,
    height=50,
    x=10,
    y=160,
    name_img="images\\npc\yes.png",
    color="green"
)

right_blue_wire = btns.Button(
    width = 110,
    height=50,
    x=720,
    y=160,
    name_img="images\\npc\yes.png",
    color="green"
)

left_red_wire = btns.Button(
    width = 110,
    height=50,
    x=10,
    y=290,
    name_img="images\\npc\yes.png",
    color="red"
)

right_red_wire = btns.Button(
    width = 110,
    height=50,
    x=720,
    y=290,
    name_img="images\\npc\yes.png",
    color="green"
)

left_blue_wire = btns.Button(
    width = 110,
    height=50,
    x=10,
    y=430,
    name_img="images\\npc\yes.png",
    color="blue"
)

right_purple_wire = btns.Button(
    width = 110,
    height=50,
    x=720,
    y=430,
    name_img="images\\npc\yes.png",
    color="green"
)

left_purple_wire = btns.Button(
    width = 110,
    height=50,
    x=10,
    y=560,
    name_img="images\\npc\yes.png",
    color="purple"
)

right_green_wire = btns.Button(
    width = 110,
    height=50,
    x=720,
    y=560,
    name_img="images\\npc\yes.png",
    color="green"
)

left_yellow_wire = btns.Button(
    width = 110,
    height=50,
    x=10,
    y=700,
    name_img="images\\npc\yes.png",
    color="yellow"
)

right_yellow_wire = btns.Button(
    width = 110,
    height=50,
    x=720,
    y=700,
    name_img="images\\npc\yes.png",
    color="green"
)

wires_list_left.append(left_green_wire)
wires_list_left.append(left_red_wire)
wires_list_left.append(left_blue_wire)
wires_list_left.append(left_purple_wire)
wires_list_left.append(left_yellow_wire)

wires_list_right.append(right_blue_wire)
wires_list_right.append(right_red_wire)
wires_list_right.append(right_purple_wire)
wires_list_right.append(right_green_wire)
wires_list_right.append(right_yellow_wire)