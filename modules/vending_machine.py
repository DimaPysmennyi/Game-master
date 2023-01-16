import pygame
import modules.player as player
import modules.settings as settings

pygame.init()

button_list = []



mouse = pygame.mouse.get_pos()
mouse_pressed = pygame.mouse.get_pressed()

def vending_machine(win):
    for button in button_list:
        button.blit_sprite(win)
    if mouse_pressed[0]:
        if mouse[0] >= button1.X and mouse[0] <= button1.X + button1.WIDTH:
            if mouse[1] >= button1.Y and mouse[1] <= button1.Y + button1.HEIGHT:
                player.hero.INVENTORY.append("screwdriver")


button1 = settings.Settings(
    width = 100,
    height = 100,
    x = 470,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button2 = settings.Settings(
    width = 100,
    height = 100,
    x = 570,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button3 = settings.Settings(
    width = 100,
    height = 100,
    x = 670,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button4 = settings.Settings(
    width = 100,
    height = 100,
    x = 470,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button5 = settings.Settings(
    width = 100,
    height = 100,
    x = 570,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button6 = settings.Settings(
    width = 100,
    height = 100,
    x = 670,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button7 = settings.Settings(
    width = 100,
    height = 100,
    x = 470,
    y = 620,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button8 = settings.Settings(
    width = 100,
    height = 100,
    x = 570,
    y = 620,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button9 = settings.Settings(
    width = 100,
    height = 100,
    x = 670,
    y = 620,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button_list.append(button1)
button_list.append(button2)
button_list.append(button3)
button_list.append(button4)
button_list.append(button5)
button_list.append(button6)
button_list.append(button7)
button_list.append(button8)
button_list.append(button9)