import pygame
import modules.buttons as btns
import modules.settings as settings
import random

p0 = False
p1 = False
p2 = False
p3 = False
p4 = False
p5 = False
p6 = False
p7 = False
p8 = False
p9 = False

bg_terminal = settings.Settings(
    width=840,
    height=840,
    x=0,
    y=0,
    name_img="images\\buttons\password_panel.png",
    color=(0,0,0)
)

input_list = []

def terminal(win):
    global p0
    global p1
    global p2
    global p3
    global p4
    global p5
    global p6
    global p7
    global p8
    global p9
    print(input_list)




    bg_terminal.blit_sprite(win)
    for bt in button_list:
        bt.draw(win)
        if bt.button_pressing():
            if bt == bt0:
                if p0 == False:
                    input_list.append("0")
                    p0 = True
            if bt == bt1:
                if p1 == False:
                    input_list.append("1")
                    p1 = True
            if bt == bt2:
                if p2 == False:
                    input_list.append("2")
                    p2 = True
            if bt == bt3:
                if p3 == False:
                    input_list.append("3")
                    p3 = True
            if bt == bt4:
                if p4 == False:
                    input_list.append("4")
                    p4 = True
            if bt == bt5:
                if p5 == False:
                    input_list.append("5")
                    p5 = True
            if bt == bt6:
                if p6 == False:
                    input_list.append("6")
                    p6 = True
            if bt == bt7:
                if p7 == False:
                    input_list.append("7")
                    p7 = True
            if bt == bt8:
                if p8 == False:
                    input_list.append("8")
                    p8 = True
            if bt == bt9:
                if p9 == False:
                    input_list.append("9")
                    p9 = True

    if len(input_list) > 4:
        input_password = input_list[0]+input_list[1]+input_list[2]+input_list[3]
        if input_password == settings.password:
            settings.terminal = True
            settings.scene = "loc4"
        
        else:
            p0 = False
            p1 = False
            p2 = False
            p3 = False
            p4 = False
            p5 = False
            p6 = False
            p7 = False
            p8 = False
            p9 = False

        input_list.clear()    

bt0 = btns.Button(
    width=60,
    height=60,
    x=390,
    y=580,
    name_img="images\wall.png",
    color=(0,0,0)
)

bt1 = btns.Button(
    width=60,
    height=60,
    x=305,
    y=345,
    name_img="images\wall.png",
    color=(0,0,0)
)

bt2 = btns.Button(
    width=60,
    height=60,
    x=390,
    y=345,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt3 = btns.Button(
    width=60,
    height=60,
    x=475,
    y=345,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt4 = btns.Button(
    width=60,
    height=60,
    x=305,
    y=425,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt5 = btns.Button(
    width=60,
    height=60,
    x=390,
    y=425,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt6 = btns.Button(
    width=60,
    height=60,
    x=475,
    y=425,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt7 = btns.Button(
    width=60,
    height=60,
    x=305,
    y=500,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt8 = btns.Button(
    width=60,
    height=60,
    x=390,
    y=500,
    name_img="images\wall.png",
    color=(0,0,0)
)
bt9 = btns.Button(
    width=60,
    height=60,
    x=475,
    y=500,
    name_img="images\wall.png",
    color=(0,0,0)
)

button_list = []

button_list.append(bt0)
button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)