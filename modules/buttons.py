import modules.settings as settings
import pygame

class Button(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def button_pressing(self):
        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0]:
            if mouse[0] >= self.X and mouse[0] <= self.X + self.WIDTH:
                if mouse[1] >= self.Y and mouse[1] <= self.Y + self.HEIGHT:
                    return True

button_list = []

button_start = Button(
    width = 420,
    height = 200,
    x = 210,
    y = 300,
    name_img="images\\buttons\\button_start.png",
    color = (0, 0, 0)
)

button_restart = Button(
    width = 420,
    height = 200,
    x = 210,
    y = 420,
    name_img="images\\buttons\\button_restart.png",
    color = (0, 0, 0)
)

button_exit = Button(
    width = 420,
    height = 200,
    x = 210,
    y = 520,
    name_img="images\\buttons\\button_exit.png",
    color = (0, 0, 0)
)

back_button = Button(
    width = 100,
    height = 50,
    x = 0,
    y = 0, 
    name_img = "images\\npc\yes.png",
    color = "black"
)
yes_button = Button(
    width = 100,
    height = 50,
    x = 610,
    y = 750,
    name_img = "images\\npc\yes.png",
    color = "black"
)

no_button = Button(
    width = 100,
    height = 50,
    x = 500,
    y = 750,
    name_img = "images\\npc\\no.png",
    color = "black"
)

skip_button = Button(
    width = 100,
    height = 50,
    x = 740,
    y = 480, 
    name_img = "images\\npc\yes.png",
    color = "black"
)

button1 = Button(
    width = 100,
    height = 100,
    x = 470,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button2 = Button(
    width = 100,
    height = 100,
    x = 570,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button3 = Button(
    width = 100,
    height = 100,
    x = 670,
    y = 420,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button4 = Button(
    width = 100,
    height = 100,
    x = 470,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button5 = Button(
    width = 100,
    height = 100,
    x = 570,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button6 = Button(
    width = 100,
    height = 100,
    x = 670,
    y = 520,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button7 = Button(
    width = 100,
    height = 100,
    x = 470,
    y = 620,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button8 = Button(
    width = 100,
    height = 100,
    x = 570,
    y = 620,
    name_img = "images\\npc\yes.png",
    color = "white"
)

button9 = Button(
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