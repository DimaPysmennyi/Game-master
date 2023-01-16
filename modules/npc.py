import pygame
import modules.settings as settings
import modules.object as object

class NPC(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.JOKE = None
        
    def dialog(self, win, head1, head2):
        dialog_win = object.Object(
            width = 840,
            height = 420,
            x = 0,
            y = 420,
            name_img = "images\\npc\dialog.png",
            color = "black"
        )


        dialog_win.blit_sprite(win)
        head1.blit_sprite(win)
        head2.load_image(direction=True)
        head2.blit_sprite(win)


    def show_text(self, text, win, size, x, y):
        font = pygame.font.SysFont('fonts\Digital_Thin.ttf', size)
        text = font.render(str(text), 1, (255,255,255), None)
        win.blit(text, (x, y))

prisoner = NPC(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img = "images\\npc\\prisoner.png",
    color = (52,198,52)
)

illya = NPC(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img = "images\\npc\\illya.png",
    color = (52,198,52)
)

security_guy = NPC(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img = "images\\npc\\security_guy.png",
    color = (52,198,52)
)