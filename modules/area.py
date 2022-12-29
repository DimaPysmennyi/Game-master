import pygame
from modules.settings import Settings
from modules.player import hero

class Area(Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

map = [
    list("bbbbbbbbbb"),
    list("b00000000b"),
    list("b0p000000b"),
    list("b00000000b"),
    list("bbb000000b"),
    list("b00000000b"),
    list("b000000bbb"),
    list("b00000000b"),
    list("b00000000b"),
    list("bbbbbbbbbb")
]

# пака ярик
list_create_area = []
list_rect = []
block_width = 80
block_height = 80


def create_area(level):
    x = 0
    y = 0

    for row in map:
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

                list_create_area.append(block)
                list_rect.append(block.RECT)

            if column == "p":
                hero.RECT.x = x
                hero.RECT.y = y
                hero.X = x
                hero.Y = y

            x += block_width
        y += block_height
        x = 0
    
create_area(map)