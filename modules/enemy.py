import modules.object as object
import modules.player as player
import modules.area as area

class Enemy(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.BULLET_DIRECTION = bullet_direction
        self.ENEMY_MOVE = True
        self.COUNT_BULLET = 0
    
    def enemy_move(self, area):
        # self.gravity(area.list_block_area)
        if self.DIRECTION == "R":
            self.col_right(area.list_block_area)
            if self.MOVE_RIGHT == False:
                self.ENEMY_MOVE = False
                self.DIRECTION = "L"
            else:
                self.ENEMY_MOVE = True
                self.X += 5
                self.RECT.x += 5

        if self.DIRECTION == "L":
            self.col_left(area.list_block_area)
            # print(self.MOVE_LEFT)
            if self.MOVE_LEFT == False:
                self.ENEMY_MOVE = False
                self.DIRECTION = "R"
                print(self.ENEMY_MOVE)
            else:
                self.ENEMY_MOVE = True
                self.X -= 5
                self.RECT.x -= 5

                              
        if self.ENEMY_MOVE == True:
            if self.DIRECTION == "L":
                self.col_left(area.list_hero)
                # print(self.MOVE_LEFT)
                if self.MOVE_LEFT == False:
                    self.DIRECTION = "R"
                    player.hero.HEALTH -= 1
                else:
                    self.ENEMY_MOVE = True
            if self.DIRECTION == "R":
                self.col_right(area.list_hero)
                # print(self.MOVE_RIGHT)
                if self.MOVE_RIGHT == False:
                    self.DIRECTION = "L"
                    player.hero.HEALTH -= 1
                else:
                    self.ENEMY_MOVE = True        
        
    def shoot(self, win, direction, count_while, width, height):
        self.COUNT_BULLET += 1
        if self.COUNT_BULLET % count_while == 0 and len(area.list_bullet) < 3:
            #  and len(self.LIST_BULLET) < 1
            bullet1 = Bullet(
                x = self.X + width,
                y = self.Y + height//2,
                width= 20,
                height= 10,
                name_img= "images\enemies\\bullet.png",
                color= (255,0,0)
            )

            area.list_bullet.append(bullet1)


        if area.list_bullet:
            for bullet1 in area.list_bullet:
                bullet1.blit_sprite(win)
                bullet1.move_bullet(direction)
                # print(bullet1.MOVE_BULLET)
                if bullet1.MOVE_BULLET == False:
                    area.list_bullet.remove(bullet1)


class Bullet(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BULLET_SPEED = 5
        self.MOVE_BULLET = False


    def move_bullet(self, direction):
        if direction == "L":
            self.col_left(area.list_block_area)
            if self.MOVE_LEFT == False: 
                self.MOVE_BULLET = False

            if self.MOVE_LEFT == True:
                self.MOVE_BULLET = True

            self.col_left(area.list_door_left)
            if self.MOVE_LEFT == False: 
                self.MOVE_BULLET = False

            if self.MOVE_LEFT == True:
                self.MOVE_BULLET = True
        
        if direction == "R":
            self.col_right(area.list_block_area)
            if self.MOVE_RIGHT == False: 
                self.MOVE_BULLET = False

            if self.MOVE_RIGHT == True:
                self.MOVE_BULLET = True

            self.col_right(area.list_door_right)
            if self.MOVE_RIGHT == False: 
                self.MOVE_BULLET = False

            if self.MOVE_RIGHT == True:
                self.MOVE_BULLET = True

        if self.MOVE_BULLET:
            if direction == "L":
                self.col_left(area.list_hero)
                if self.MOVE_LEFT == False:
                    self.MOVE_BULLET = False
                    player.hero.HEALTH -= 1
                else:
                    self.MOVE_BULLET = True

            if direction == "R":
                self.col_right(area.list_hero)
                if self.MOVE_RIGHT == False:
                    self.MOVE_BULLET = False
                    player.hero.HEALTH -= 1
                else:
                    self.MOVE_BULLET = True        
                    
        if self.RECT.x <= 0 or self.RECT.x >= 840:
            self.MOVE_BULLET = False

        if self.MOVE_BULLET:
            if direction == "L":
                self.RECT.x -= self.BULLET_SPEED
                self.X -= self.BULLET_SPEED
            else:
                self.RECT.x += self.BULLET_SPEED
                self.X += self.BULLET_SPEED                

turret = Enemy(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img="images\enemies\\turret.png",
    color = (192, 61, 225)
)

siren = Enemy(
    width = 45,
    height = 55,
    x = 0,
    y = 0,
    name_img="images\enemies\siren.png",
    color = (192, 61, 225)
)