import pygame
import os

scene = "menu"

def find_path():
    path_image = os.path.abspath(__file__ + "/..")
    path_image = path_image.split("\\") 
    del path_image[-1]
    path_image = "\\".join(path_image)
    return path_image

class Settings:
    def __init__(self, width = None, height = None, x = None, y = None, name_img = None, color=None):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.NAME_IMG = name_img
        self.IMAGE = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.RECT = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        self.COLOR = color
        self.load_image()
    

    def load_image(self, direction=False):
        path_image = find_path()
        path_image = os.path.join(path_image, self.NAME_IMG)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE, direction, False)
  

        # for frame in frame_list:
        #     load_frame = 
        #     win.blit(frame, (self.X, self.Y))
        


    def blit_sprite(self, win):
        win.blit(self.IMAGE, (self.X, self.Y))
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.RECT)
        

button_start = Settings(
    width = 420,
    height = 200,
    x = 210,
    y = 300,
    name_img="images\\buttons\\button_start.png",
    color = (0, 0, 0)
)


button_exit = Settings(
    width = 420,
    height = 200,
    x = 210,
    y = 520,
    name_img="images\\buttons\\button_exit.png",
    color = (0, 0, 0)
)
button = Settings(
    width = 420,
    height = 200,
    x = 210,
    y = 420,
    name_img="images\\buttons\\button_restart.png",
    color = (0, 0, 0)
)

bg1 = Settings(
    width = 720,
    height = 720,
    x = 60,
    y = 60,
    name_img = "images\\bg.png",
    color = "gray"
)

bg2 = Settings(
    width = 720,
    height = 720,
    x = 60,
    y = 60,
    name_img = "images\\bg2.png",
    color = "gray"
)

bg_death = Settings(
    width = 840,
    height = 840,
    x = 0,
    y = 0,
    name_img = "images\\death_bg.png",
    color = "gray"
)

bg_menu = Settings(
    width = 840,
    height = 840,
    x = 0,
    y = 0,
    name_img = "images\\start_bg.png",
    color = "gray"
)

cutscene = Settings(
    width = 840,
    height = 840,
    x = 0,
    y = 0,
    name_img = "images\\cutscene1.png",
    color = "gray"
)

lever = Settings(
    width= 30,
    height = 30,
    x = 700,
    y = 184,
    name_img = "images\lever_off.png",
    color = "green"            
)

lever2 = Settings(
    width= 30,
    height = 30,
    x = 700,
    y = 424,
    name_img = "images\lever_off.png",
    color = "green"            
)

lever3 = Settings(
    width= 30,
    height = 30,
    x = 700,
    y = 184,
    name_img = "images\lever_off.png",
    color = "green"            
)


trapdoor_pressed = False
trapdoor2_pressed = False
laser_pressed = False

player_head = Settings(
    width = 170,
    height = 140,
    x = 110,
    y = 480,
    name_img = "images\\npc\player_head.png",
    color = "black"
)
prisoner_head = Settings(
    width = 160,
    height = 140,
    x = 580,
    y = 480,
    name_img = "images\\npc\\prisoner_head.png",
    color = "black"
)

illya_head = Settings(
    width = 160,
    height = 140,
    x = 580,
    y = 480,
    name_img = "images\\npc\\illya_head.png",
    color = "black"
)

security_guy_head = Settings(
    width = 160,
    height = 140,
    x = 580,
    y = 480,
    name_img = "images\\npc\\security_guy_head.png",
    color = "black"
)

yes_button = Settings(
    width = 100,
    height = 50,
    x = 610,
    y = 750,
    name_img = "images\\npc\yes.png",
    color = "black"
)

no_button = Settings(
    width = 100,
    height = 50,
    x = 500,
    y = 750,
    name_img = "images\\npc\\no.png",
    color = "black"
)

skip_button = Settings(
    width = 100,
    height = 50,
    x = 740,
    y = 480, 
    name_img = "images\\npc\yes.png",
    color = "black"
)

# слабо слабо слабо
bed = Settings(
    width = 100,
    height = 80,
    x = 60,
    y = 175,
    name_img = "images\\bed.png",
    color = "black"
)

laser = Settings(
    width = 60,
    height = 60,
    x = 0,
    y = 0,
    name_img = "images\\laser.png",
    color = "black"
)

ladder = Settings(
    width = 60,
    height = 60,
    x = 0,
    y = 0,
    name_img="images\ladder.png",
    color = (0, 0, 0)
)

vending_machine = Settings(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img="images\gas.png",
    color = (0, 0, 0)
)

keys = Settings(
    width = 60,
    height = 60,
    x = 540,
    y = 600,
    name_img="images\keys.png",
    color = (0, 0, 0)
)

back_button = Settings(
    width = 100,
    height = 50,
    x = 0,
    y = 0, 
    name_img = "images\\npc\yes.png",
    color = "black"
)

cutscene_speed = 0
vending_machine_pressed = False