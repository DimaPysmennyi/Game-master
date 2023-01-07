
import modules.settings as settings
from modules.player import hero
from modules.levels import *
from modules.enemy import turret, siren
from modules.npc import prisoner

class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

map = [level1, level2, level3]
# пака ярик
list_block_area = []
block_width = 60
block_height = 60

list_door_right = []
list_door_left = []

list_turrets = []
list_bullet = []

list_hero = []
list_npc = []

list_lever = []
list_lever.append(settings.lever)

list_siren = []

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
                # list_block_rect.append(block.RECT)

            if column == "p":
                hero.RECT.x = x
                hero.RECT.y = y
                hero.X = x
                hero.Y = y
                
                list_hero.append(hero)
                
            
            if column == "r":
                door_right = Area(
                    width = block_width,
                    height = block_height,
                    x = x,
                    y = y,
                    name_img = "images\door.png",
                    color = "yellow"
                )
                list_door_right.append(door_right)
                # list_door_right_rect.append(door_right.RECT)

            if column == "l":
                door_left = Area(
                    width = block_width,
                    height = block_height,
                    x = x,
                    y = y,
                    name_img = "images\door.png",
                    color = "yellow"
                )

                list_door_left.append(door_left)
                # list_door_right_rect.append(door_left.RECT)

            if column == "t":
                turret.RECT.x = x
                turret.RECT.y = y
                turret.X = x
                turret.Y = y
                list_turrets.append(turret)
                # list_turrets_rect.append(turret)

            if column == "n":
                prisoner.RECT.x = x 
                prisoner.RECT.y = y + 4
                prisoner.Y = y + 4 
                prisoner.X = x

                list_npc.append(prisoner)

            if column == "d":   
                settings.trapdoor.RECT.x = x
                settings.trapdoor.RECT.y = y
                settings.trapdoor.X = x
                settings.trapdoor.Y = y

                list_block_area.append(settings.trapdoor)
            
            if column == "s":
                siren.X = x
                siren.RECT.x = x
                siren.Y = y
                siren.RECT.y = y

                list_siren.append(siren)

            x += block_width
        y += block_height
        x = 0

print(level1)
create_area()