import Data

class Hero:
    def __init__(self,x,y,name):

        self.Name=name
        heros_atributes = Heros_Data.Heros_Dic[name]
        self.Position_x=x
        self.Position_y=y
        self.Speed_Rate=heros_atributes["SPEED_RATE"]
        self.Health=heros_atributes["HEALTH"]
        self.Bullet=heros_atributes["BULLET"]
        self.Damage_Rate=heros_atributes["DAMAGE_RATE"]


'''
    REQUIERFD:
    
        SPEED
        POSITION
        HEALTH
        DAMAGE_RATE
        DAMAGE_TYPE        



'''