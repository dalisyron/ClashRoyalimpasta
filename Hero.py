import Data,Bullet

class Hero:
    def __init__(self,x,y,name_,side_):

        self.name=name_
        self.side=side_
        heros_atributes = Data.Heros_Dic[name_]
        self.position_x=x
        self.position_y=y
        self.speed_Rate=heros_atributes["SPEED_RATE"]
        self.health=heros_atributes["HEALTH"]
        self.bullet=heros_atributes["BULLET"]
        self.damage_Rate=heros_atributes["DAMAGE_RATE"]




def herosProcess(grid,currentHeros,currentBullets,Cnt):
    
    for hero in currentHeros[0]:
        if Cnt % hero.speed_Rate == 0:
            
            hero.position_x+=1
            # bayad hero.nextPostion() bashe
    for hero in currentHeros[1]:
        if Cnt % hero.speed_Rate == 0:
            hero.position_x-=1

        if Cnt % hero.damage_Rate == 0:
            newBullet = Bullet.Bullet(hero.position_x , hero.position_y , hero.position_x+130 ,hero.position_y+130,hero.bullet,hero.side) # bayad dorost hesabi mosahkhs she in example e
            currentBullets.append(newBullet)





            

    


    
'''
    REQUIERFD:
    
        SPEED
        POSITION
        HEALTH
        DAMAGE_RATE
        DAMAGE_TYPE        



'''
