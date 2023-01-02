
from modules.settings import Settings
from modules.player import hero
from modules.levels import *

class Area(Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

map = [level1, level2, level3, level4, level5, level6, level7]

# пака ярик
list_block_area = []
list_block_rect = []
block_width = 60
block_height = 60

list_door_right = []
list_door_right_rect = []
list_door_left = []
list_door_left_rect = []



def create_area():
    x = 0
    y = 0
    for row in map[hero.CURRENT_LEVEL]:
        for column in row:
            if column == "b":
                block = Area(
                    width = block_width,
                    height = block_height,
                    x = x,
                    y = y,
                    name_img = "images\\wall.png",
                    color = "green"
                )

                list_block_area.append(block)
                list_block_rect.append(block.RECT)

            if column == "p":
                hero.RECT.x = x
                hero.RECT.y = y
                hero.X = x
                hero.Y = y
            
            if column == "r":
                door_right = Area(
                    width = block_width,
                    height = block_height,
                    x = x,
                    y = y,
                    name_img = "images\\door.png",
                    color = "yellow"
                )
                list_door_right.append(door_right)
                list_door_right_rect.append(door_right.RECT)

            if column == "l":
                door_left = Area(
                    width = block_width,
                    height = block_height,
                    x = x,
                    y = y,
                    name_img = "images\\door.png",
                    color = "yellow"
                )

                list_door_left.append(door_left)
                list_door_right_rect.append(door_left.RECT)

            x += block_width
        y += block_height
        x = 0
    
create_area()