import pygame
import modules.settings as settings
import modules.object as object

class NPC(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def dialog(self, dialog_text, win):
        dialog_win = object.Object(
                width = 840,
                height = 420,
                x = 0,
                y = 420,
                name_img = "images\\npc\dialog.png",
                color = "black"
        )
        player_head = object.Object(
                width = 160,
                height = 140,
                x = 120,
                y = 480,
                name_img = "images\\npc\player_head.png",
                color = "black"
        )
        npc_head = object.Object(
                width = 160,
                height = 140,
                x = 580,
                y = 480,
                name_img = "images\\npc\\prisoner_head.png",
                color = "black"
        )
        dialog_win.blit_sprite(win)
        player_head.blit_sprite(win)
        npc_head.load_image(direction=True)
        npc_head.blit_sprite(win)
        font = pygame.font.SysFont('fonts\Digital_Thin.ttf', 39)
        text = font.render(str(dialog_text), 1, (255,255,255), None)
        win.blit(text, (51, 700))

prisoner = NPC(
    width = 40,
    height = 55,
    x = 0,
    y = 0,
    name_img = "images\\npc\\prisoner.png",
    color = (52,198,52)
)