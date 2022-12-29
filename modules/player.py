import modules.settings as settings
import modules.area as area
import modules.object as object
import pygame


class Player(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.HEALTH = 10
        self.MOVE_DOWN = False
        self.DIRECTION = "R"
        self.MOVE_RIGHT = False
        self.MOVE_LEFT = False
        self.MOVE_UP = False
        self.MOVE_DOWN = False
        self.GRAVITY = True
        self.MAX_JUMP = 200
    

    def move(self, area):

        # self.col_down(area)
        self.gravity(area)

        event = pygame.key.get_pressed()

        self.col_up(area)

        if event[pygame.K_d]:
            self.col_right(area)
            if self.MOVE_RIGHT == True:
                self.X += 5
                self.RECT.x += 5
                self.DIRECTION = "R"
                # self.animation(folder="Player", count_while=4, first_img=1, last_img=5)

        if event[pygame.K_a]:
            self.col_left(area)
            if self.MOVE_LEFT == True:
                self.X -= 5
                self.RECT.x -= 5
                self.DIRECTION = "L"

        if event[pygame.K_w]:
            self.col_down(area)
            self.col_up(area)
            if self.MOVE_UP == True:
                pass
                # павсет иди спи
                # властелин чего 
                # или ничего
                # чего
                # или ничего
                # дверь мне сделал 
                # чел кринж
                

                # self.GRAVITY = False
                # self.Y -= 2
                # self.RECT.y -= 2
                # self.MAX_JUMP -= 1
                # self.MOVE_DOWN = False
                # if self.MAX_JUMP == 0:
                    # self.MOVE_DOWN = True
                    # self.MAX_JUMP = 200
            # else:
                # self.MOVE_DOWN = True
            # 

            



    # # def animation(self, folder=None, count_while=None, first_img=None, last_img=None):
    #     self.SPEED_ANIMATION += 1
    #     if self.SPEED_ANIMATION % count_while == 0:
    #         if self.COUNT_IMG == last_img:
    #             self.COUNT_IMG = first_img
    #         self.NAME_IMG = f"images\\{folder}\\{self.COUNT_IMG}.png"
    #         self.direction()
    #         self.COUNT_IMG += 1
    #     self.COUNT_IMG = 1
        
    # def direction(self):
    #     if self.DIRECTION == "R":
    #         self.load_image()
    #     if self.DIRECTION == "L":
    #         self.load_image(direction=True)
    
    def damage(self, damage):
        self.HEALTH -= damage
    
    # def heal(self, add_health):

    
    #health_width = 30
    #health_height = 5

    def health_font(self, win):
        self.load_image()
        font = pygame.font.SysFont('arial', 60)
        text = font.render(str(self.HEALTH), 1, (255,69,0), None)
        win.blit(text, (65, 0))
        heart_sprite = settings.Settings(
            width = 60,
            height = 60, 
            x = 0,
            y = 0,
            name_img="images\\health.png",
            color = "yellow"
        )    
        heart_sprite.blit_sprite(win)


    def die(self, win):
        font = pygame.font.SysFont('arial', 40)
        text = font.render('САЛАМ МАЛЕКУ', 1, (255, 255, 255), None)
        win.blit(text, (200, 200))
    
hero = Player(
    width = 50,
    height = 70,
    x = 0,
    y = 0,
    name_img = "images\\Player\\1.png",
    color = "red"
) 