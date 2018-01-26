import Data , grid

class Bullet:

    def __init__(self,x1,y1,x2,y2,name,side_):
        self.Name=name
        self.side=side_
        bullet_atributes=Data.Bullets_Dic[name]
        self.position_x=x1
        self.position_y = y1
        self.dest_x = x2
        self.dest_y = y2
        self.range = bullet_atributes["RANGE"]
        self.damage = bullet_atributes["DAMAGE"]
        self.speed = bullet_atributes["SPEED"]
        self.is_destroyed = False








def bulletsProcess(currentBullets):
    for bullet in currentBullets:
        if bullet.is_destroyed == False:
            dx=bullet.dest_x - bullet.position_x
            dy=bullet.dest_y - bullet.position_y
            d=(dx**2 + dy**2)**0.5
            if d < 4:
                bullet.is_destroyed = True
                continue
                #yani tamom shod masiresho raft
            vx=bullet.speed*(dx/d)
            vy=bullet.speed*(dy/d)
            bullet.position_x+=vx
            bullet.position_y+=vy
          #  checkForHit()  tabdil pos be grid va inke to grid che obj ee hast baad damage va az bein raftan bullet




'''

    REQUIERED:
    
        SOURCE
        POSITION
        DEST
        VELOCITY_VECTOR
        DAMAGE
        SIDE
        RANGE



    OPIONAL
    
        ISAEREAL


'''

