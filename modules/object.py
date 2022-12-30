import pygame
import modules.area as area 
import modules.settings as settings


class Object(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.GRAVITY = True

    def col_right(self, list_walls):
       for wall in list_walls:
           if self.Y <= wall.Y + wall.HEIGHT and self.Y + self.HEIGHT >= wall.Y:
               if self.X + self.WIDTH >= wall.X - 5  and self.X <= wall.X:
                   self.MOVE_RIGHT = False
                   break
               else:
                   self.MOVE_RIGHT = True
                   
           else:
               self.MOVE_RIGHT = True

                                
    def col_left(self, list_walls):
         for wall in list_walls:
            if self.Y <= wall.Y + wall.HEIGHT and self.Y + self.HEIGHT >= wall.Y:
                if self.X <= wall.X + wall.WIDTH + 5 and self.X >= wall.X:
                    self.MOVE_LEFT = False
                    break
                else:
                    self.MOVE_LEFT = True
                    
            else:
                self.MOVE_LEFT = True

    def col_down(self, list_walls):
        for wall in list_walls:
            if self.X <= wall.X + wall.WIDTH and self.X + self.WIDTH >= wall.X:
                if self.Y + self.HEIGHT >= wall.Y - 1 and self.Y <= wall.Y:
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
            self.Y += 1
            self.RECT.y += 1
            # self.GRAVITY = True
        else:
            self.GRAVITY = False
        
    
        
    #         obj.GRAVITY = False
    #     else:
    #         obj.GRAVITY = True

    # if obj.GRAVTITY == True:
