import pygame
import modules.settings as settings



class Object(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DIRECTION = "R"
        self.GRAVITY_SPEED = 2
        self.GRAVITY = True
        self.SHOW_DIALOG = False
        self.JUMP = False

        self.COUNT_IMG = 0
        self.SPEED_ANIMATION = 0
        self.CURRENT_LEVEL = 0
        self.CURRENT_MAP = 0

    def col_right(self, list_walls):
       for wall in list_walls:
           if self.Y <= wall.Y + wall.HEIGHT and self.Y + self.HEIGHT >= wall.Y:
               if self.X + self.WIDTH >= wall.X - 5 and self.X <= wall.X:
                   self.MOVE_RIGHT = False
                #    print("da")
                   break
               else:
                   self.MOVE_RIGHT = True
                   
           else:
               self.MOVE_RIGHT = True

                                
    def col_left(self, list_walls):
         for wall in list_walls:
            if self.Y <= wall.Y + wall.HEIGHT and self.Y + self.HEIGHT >= wall.Y:
                if self.X <= wall.X + wall.WIDTH + 5 and self.X >= wall.X:
                    # print("da")
                    self.MOVE_LEFT = False
                    break
                else:
                    self.MOVE_LEFT = True
                    
            else:
                self.MOVE_LEFT = True

    def col_down(self, list_walls):
        for wall in list_walls:
            if self.X <= wall.X + wall.WIDTH and self.X + self.WIDTH >= wall.X:
                if self.Y + self.HEIGHT >= wall.Y - self.GRAVITY_SPEED and self.Y <= wall.Y:
                    self.MOVE_DOWN = False
                    break
                
                else:
                    self.MOVE_DOWN = True
            else:
                self.MOVE_DOWN = True

    def col_up(self, list_walls):
        for wall in list_walls:
            if self.X <= wall.X + wall.WIDTH and self.X + self.WIDTH >= wall.X:
                if self.Y <= wall.Y + wall.HEIGHT + self.SPEED_JUMP and self.Y >= wall.Y:
                    self.JUMP = False
                    self.MOVE_DOWN = True

                    break

    def gravity(self, area):
        self.col_down(area)
        if self.MOVE_DOWN == True and self.JUMP == False:
            self.Y += self.GRAVITY_SPEED
            self.RECT.y += self.GRAVITY_SPEED
            # self.GRAVITY = True
        else:
            self.GRAVITY = False
        
    def animation(self, folder, first_img, last_img):
        if self.COUNT_IMG > last_img or self.COUNT_IMG < 0:
            self.COUNT_IMG = first_img

        else:
            if self.SPEED_ANIMATION == 4:   
                self.NAME_IMG = f"images\{folder}\{self.COUNT_IMG}.png"
                if first_img > last_img:
                    self.COUNT_IMG -= 1

                if first_img < last_img:
                    self.COUNT_IMG += 1
                self.SPEED_ANIMATION = 0

            self.SPEED_ANIMATION += 1

    def direction(self):
        if self.DIRECTION == "R":
            self.load_image()
        if self.DIRECTION == "L":
            self.load_image(direction=True)
        

