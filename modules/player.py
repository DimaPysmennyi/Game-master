import modules.settings as settings
import modules.object as object
import modules.npc as npc
# import modules.enemy as enemy

import pygame


class Player(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.HEALTH = 3
        self.MOVE_DOWN = False
        self.MOVE_RIGHT = False
        self.MOVE_LEFT = False
        self.MOVE_DOWN = False
        self.GRAVITY = False
        self.JUMP = False
        self.SHOW_DIALOG = False
        self.MAX_JUMP = 200
        self.SPEED_JUMP = 4

    def move(self, area):

        # self.col_down(area)
    
        self.gravity(area)

        event = pygame.key.get_pressed()

        self.col_up(area)

        if event[pygame.K_d]:
            self.col_right(area)
            self.DIRECTION = "R"
            if self.MOVE_RIGHT == True:
                self.X += 5
                self.RECT.x += 5

            self.animation("Player", 1, 3)
            self.direction()

        if event[pygame.K_a]:
            self.col_left(area)
            self.DIRECTION = "L"
            if self.MOVE_LEFT == True:
                self.X -= 5
                self.RECT.x -= 5
            self.animation("Player", 1, 3)
            self.direction()

        if event[pygame.K_w] and self.JUMP == False and self.GRAVITY == False:
            self.JUMP = True

        if event[pygame.K_e]:
            if self.SHOW_DIALOG == False and self.RECT.x + 50 >= npc.prisoner.RECT.x:
                self.SHOW_DIALOG = True
            if self.SHOW_DIALOG == False and self.RECT.x - 50 <= npc.prisoner.RECT.x:
                self.SHOW_DIALOG = True
            
            if settings.trapdoor_pressed == False:
                if self.X + 10 >= settings.lever.X:
                    settings.trapdoor_pressed = True




              

        if self.SHOW_DIALOG == True and self.RECT.x - 50 > npc.prisoner.RECT.x:
            self.SHOW_DIALOG = False
        
        if self.SHOW_DIALOG == True and self.RECT.x + 50 < npc.prisoner.RECT.x:
            self.SHOW_DIALOG = False

        if self.JUMP == True:
            self.col_up(area)
            self.RECT.y -= self.SPEED_JUMP
            self.Y -= self.SPEED_JUMP
            self.MAX_JUMP -= self.SPEED_JUMP
            self.GRAVITY = False
            if self.MAX_JUMP == 0:
                self.JUMP = False
                self.MAX_JUMP = 200
                self.GRAVITY = True
        
        if self.MOVE_DOWN == True:
            self.GRAVITY = True

     

        if not event:
            self.NAME_IMG = "images\Player\\0.png"
            self.direction()
        
    



    def exit(self, area):
        for door in area.list_door_right:
            if self.RECT.x >= door.RECT.x and self.RECT.y >= door.RECT.y:
                area.list_block_area.clear()
                # area.list_block_rect.clear()
                area.list_door_right.clear()
                # area.list_door_right_rect.clear()
                area.list_door_left.clear()
                # area.list_door_left_rect.clear()
                area.list_turrets.clear()
                # area.list_turrets_rect.clear()
                area.list_bullet.clear()
                area.list_npc.clear()
                area.list_lever.clear()
                area.list_siren.clear()
                
                self.CURRENT_LEVEL += 1
                area.create_area()

        for door in area.list_door_left:
            if self.RECT.x <= door.RECT.x and self.RECT.y >= door.RECT.y:
                area.list_block_area.clear()
                area.list_door_right.clear()
                area.list_door_left.clear()
                # area.list_door_left_rect.clear()
                area.list_turrets.clear()
                # area.list_turrets_rect.clear()
                area.list_bullet.clear()
                area.list_lever.clear()
                area.list_npc.clear()
                area.list_siren.clear()
                
                self.CURRENT_LEVEL -= 1
                area.create_area()

    def health_font(self, win):
        self.load_image()
        bg_health = settings.Settings(
            width = 270,
            height = 200, 
            x = -75,
            y = -80,
            name_img="images\Player\health_bg.png",
            color = "yellow"
        )
        bg_health.blit_sprite(win)
        font = pygame.font.SysFont('fonts\Digital_Thin.ttf', 100)
        text = font.render(str(self.HEALTH), 1, (225,22,25), None)
        win.blit(text, (70, 10))
        heart_sprite = settings.Settings(
            width = 60,
            height = 60, 
            x = 5,
            y = 10,
            name_img="images\Player\health.png",
            color = "yellow"
        )    
        heart_sprite.blit_sprite(win)


    def die(self):
        settings.scene = "game_over"
    
    
hero = Player(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img = "images\\Player\\0.png",
    color = "red"
) 