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
                    self.MOVE_UP = True
                    break
                
                else:
                    self.MOVE_DOWN = True
                    self.MOVE_UP = False
            else:
                self.MOVE_DOWN = True
                self.MOVE_UP = False

    def col_up(self, list_walls):
        for wall in list_walls:
            if self.X <= wall.X + wall.WIDTH and self.X + self.WIDTH >= wall.X:
                if self.Y <= wall.Y + wall.HEIGHT + 1 and self.Y >= wall.Y:
                    self.MOVE_UP = False
                    self.MOVE_DOWN = True
                    break
                else:
                    self.MOVE_UP = True
                    self.MOVE_DOWN = False
            else:
                self.MOVE_UP = True
                self.MOVE_DOWN = False

    def gravity(self, area):
        self.col_down(area)
        if self.MOVE_DOWN == True:
            self.Y += 1
            self.RECT.y += 1
        
    
        
    #         obj.GRAVITY = False
    #     else:
    #         obj.GRAVITY = True

    # if obj.GRAVTITY == True:
