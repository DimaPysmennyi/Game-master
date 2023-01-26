import modules.buttons as btns
import modules.settings as settings
import pygame

pygame.init()

button_list_left = []
button_list_right = []
left_pressed = False
right_pressed = False
left_correct = False
right_correct = False


def minigame1(win):
    global left_pressed
    global right_pressed
    global left_correct
    global right_correct

    settings.bg_minigame.blit_sprite(win)

    for bl in button_list_left:
        bl.blit_sprite(win)

    if left_pressed == False:
        if left_1.button_pressing() or left_2.button_pressing() or left_8.button_pressing() or left_9.button_pressing():
            if left_8.button_pressing() == True:
                left_correct = True
        
            left_pressed = True
            right_pressed = False

    for br in button_list_right:
        br.blit_sprite(win)

    if left_pressed == True:
        if right_pressed == False:
            if right_1.button_pressing() or right_4.button_pressing() or right_5.button_pressing() or right_7.button_pressing():
                if right_7.button_pressing() == True:
                    right_correct = True
                else:
                    left_correct = False
                    right_correct = False
                right_pressed = True
                left_pressed = False

    if left_correct == True and right_correct == True:
        font = pygame.font.SysFont("fonts\Digital_Thin.ttf", 100)
        settings.password1.blit_sprite(win)        
        text = font.render(str(settings.password), 1, (0,0,0), None)
        win.blit(text, (200, 300))

left_8 = btns.Button(
    width=100,
    height=100,
    x=10,
    y=320,
    name_img = "images\\buttons\\8.png",
    color = "purple"
)

left_1 = btns.Button(
    width=100,
    height=100,
    x=10,
    y=420,
    name_img = "images\\buttons\\1.png",
    color = "purple"
)

left_9 = btns.Button(
    width=100,
    height=100,
    x=10,
    y=520,
    name_img = "images\\buttons\\9.png",
    color = "purple"
)

left_2 = btns.Button(
    width=100,
    height=100,
    x=10,
    y=620,
    name_img = "images\\buttons\\2.png",
    color = "purple"
)

right_4 = btns.Button(
    width=100,
    height=100,
    x=730,
    y=320,
    name_img = "images\\buttons\\4.png",
    color = "purple"
)
right_1 = btns.Button(
    width=100,
    height=100,
    x=730,
    y=420,
    name_img = "images\\buttons\\1.png",
    color = "purple"
)
right_5 = btns.Button(
    width=100,
    height=100,
    x=730,
    y=520,
    name_img = "images\\buttons\\5.png",
    color = "purple"
)
right_7 = btns.Button(
    width=100,
    height=100,
    x=730,
    y=620,
    name_img = "images\\buttons\\7.png",
    color = "purple"
)

button_list_left.append(left_1)
button_list_left.append(left_2)
button_list_left.append(left_8)
button_list_left.append(left_9)

button_list_right.append(right_1)
button_list_right.append(right_4)
button_list_right.append(right_5)
button_list_right.append(right_7)