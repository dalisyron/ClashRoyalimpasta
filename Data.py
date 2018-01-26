import pygame

Heros_Dic={"Big_Hero" :
               {"DAMAGE_RATE":90 ,
                "SPEED_RATE":15,
                "HEALTH":100,
                "BULLET":"Sword" ,
                'IMAGE':{0:pygame.image.load('Images/Big_Hero.gif'), 1:pygame.image.load('Images/Big_Hero1.gif')}},
           "Knight" :{
               "DAMAGE_RATE":90 ,
               "SPEED_RATE":15,
               "HEALTH":100,
               "BULLET":"Sword",
                'IMAGE':{0:pygame.image.load('Images/Knight.gif'), 1:pygame.image.load('Images/Knight1.gif')}}
           }

Bullets_Dic={"Sword" : {"DAMAGE" : 30 , "SPEED" : 3 , "RANGE" : 2 }}
