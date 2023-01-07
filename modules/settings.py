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

button_restart = Settings(
    width = 420,
    height = 200,
    x = 210,
    y = 300,
    name_img="images\\buttons\\button_start.png",
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

lever = Settings(
    width= 20,
    height = 20,
    x = 700,
    y = 200,
    name_img = "images\lever.png",
    color = "green"            
)

trapdoor = Settings(
    width = 60,
    height = 60,
    x = 0,
    y = 0,
    name_img = "images\\trapdoor.png",
    color = "red"
)


trapdoor_pressed = False