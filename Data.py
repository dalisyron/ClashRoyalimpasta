import pygame

Heros_Dic={"Big_Hero" :
               {"DAMAGE_RATE":40 ,
                "SPEED_RATE":25,
                "HEALTH":100,
                "BULLET":"Gun" ,
                "LOADTIME":5000,
                'IMAGE':{0:pygame.image.load('Images/Big_Hero.gif'), 1:pygame.image.load('Images/Big_Hero1.gif')}},
           "Knight" :{
               "DAMAGE_RATE":90 ,
               "SPEED_RATE":10,
               "HEALTH":100,
               "BULLET":"Sword",
               "LOADTIME":1000,
                'IMAGE':{0:pygame.image.load('Images/Knight.gif'), 1:pygame.image.load('Images/Knight1.gif')}},
            "Big_Tower" :{
                "DAMAGE_RATE":90 ,
                "SPEED_RATE":10,
                "HEALTH":500,
                "BULLET":"Sword",
                "LOADTIME":1000000,
                'IMAGE':{0:pygame.image.load('Images/tall_tower.png'), 1:pygame.image.load('Images/tall_tower.png')}},
            "Small_Tower" :{
                "DAMAGE_RATE":90 ,
                "SPEED_RATE":10,
                "HEALTH":250,
                "BULLET":"Sword",
                "LOADTIME":1000000,
                'IMAGE':{0:pygame.image.load('Images/small_tower.png'), 1:pygame.image.load('Images/small_tower.png')}}
           }

Bullets_Dic={"Sword" : {"DAMAGE" : 40 , "SPEED" : 3 , "RANGE" : 2 },
             "Gun" : {"DAMAGE" : 30 , "SPEED" : 6 , "RANGE" : 4 }}

