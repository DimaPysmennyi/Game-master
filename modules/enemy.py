import modules.object as object
import modules.player as player
import modules.area as area

class Enemy(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.BULLET_DIRECTION = bullet_direction
        self.COUNT_BULLET = 0
    
    def shoot(self, win, count_while, width, height):
        self.COUNT_BULLET += 1
        if self.COUNT_BULLET % count_while == 0 and len(area.list_bullet) < 3:
            #  and len(self.LIST_BULLET) < 1
            bullet1 = Bullet(
                x = self.X - width,
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
                bullet1.move_bullet()
                print(bullet1.MOVE_BULLET)
                if bullet1.MOVE_BULLET == False:
                    area.list_bullet.remove(bullet1)


class Bullet(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BULLET_SPEED = 5
        self.MOVE_BULLET = False


    def move_bullet(self):
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

        if self.MOVE_BULLET:
            self.col_left(area.list_hero)
            if self.MOVE_LEFT == False:
                self.MOVE_BULLET = False
                player.hero.HEALTH -= 1
            else:
                self.MOVE_BULLET = True

        if self.RECT.x <= 0:
            self.MOVE_BULLET = False

        if self.MOVE_BULLET:
            self.RECT.x -= self.BULLET_SPEED
            self.X -= self.BULLET_SPEED

turret = Enemy(
    width = 40,
    height = 55,
    x = 0,
    y = 0,
    name_img="images\enemies\\turret.png",
    color = (192, 61, 225)
)
