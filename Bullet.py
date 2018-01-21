import Data

class Bullet:

    def __init__(self,x1,y1,x2,y2,name):
        self.Name=name
        bullet_atributes=Data.Bullets_Dic[name]
        self.Position_x=x1
        self.Position_y = y1
        self.Dest_x = x2
        self.Dest_y = y2
        self.Range = bullet_atributes["RANGE"]
        self.Damage = bullet_atributes["DAMAGE"]
        self.Speed = bullet_atributes["SPEED"]



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

