import modules.object as object

class Enemy(object.Object):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.TURRET = False


class Bullet(Enemy):
    def __init__(self, bullet_direction = None, **kwargs):
        super().__init__(**kwargs)
        self.BULLET_DIRECTION = bullet_direction
        self.BULLET_SPEED = 1

    def bullet_move(self):
        if self.BULLET_DIRECTION == "R":
            self.RECT.x += self.BULLET_SPEED
            self.X += self.BULLET_SPEED
        
        if self.BULLET_DIRECTION == "L":
            self.RECT.x -= self.BULLET_SPEED
            self.X -= self.BULLET_SPEED

turret = Enemy(
    width = 40,
    height = 55,
    x = 760,
    y = 760,
    name_img="images\\button_start.png",
    color = (192, 61, 225)
)

bullet = Bullet(
    bullet_direction = "L",
    width = 4,
    height = 3,
    x = turret.X,
    y = turret.Y,
    name_img="images\\button_start.png",
    color = (255, 255, 255)
)