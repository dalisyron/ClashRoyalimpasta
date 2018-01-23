import pygame

Heros_Dic={"Big_Hero" :
               {"DAMAGE_RATE":90 ,
                "SPEED_RATE":10,
                "HEALTH":100,
                "BULLET":None ,
                'IMAGE':{0:pygame.image.load('Images/Big_Hero.gif'), 1:pygame.image.load('Images/Big_Hero1.gif')}},
           "Knight" :{
               "DAMAGE_RATE":90 ,
               "SPEED_RATE":10,
               "HEALTH":100,
               "BULLET":"Sword",
                'IMAGE':{0:pygame.image.load('Images/Knight.gif'), 1:pygame.image.load('Images/Knight1.gif')}}
           }

Bullets_Dic={"Sword" : {"DAMAGE" : 30 , "SPEED" : 40 , "RANGE" : 3 }}
