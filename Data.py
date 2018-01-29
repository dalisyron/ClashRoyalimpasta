import pygame

Heros_Dic={"Viking" :
               {"DAMAGE_RATE":40 ,
                "SPEED_RATE":80,
                "HEALTH":500,
                "BULLET":"Gun" ,
                "LOADTIME":5000,
                'IMAGE':{0:pygame.image.load('Images/Viking.png'), 1:pygame.image.load('Images/Viking1.png')}},
           "Knight" :{
               "DAMAGE_RATE":30 ,
               "SPEED_RATE":40,
               "HEALTH":100,
               "BULLET":"Sword",
               "LOADTIME":3000,
                'IMAGE':{0:pygame.image.load('Images/Knight.png'), 1:pygame.image.load('Images/Knight1.png')}},
           "Soldier" :{
              "DAMAGE_RATE":30 ,
              "SPEED_RATE":30,
              "HEALTH":100,
              "BULLET":"Gun",
              "LOADTIME":1000,
              'IMAGE':{0:pygame.image.load('Images/Soldier.gif'), 1:pygame.image.load('Images/Soldier1.gif')}},
              "Ninja" :{
              "DAMAGE_RATE":60 ,
              "SPEED_RATE":30,
              "HEALTH":100,
              "BULLET":"KATAN",
              "LOADTIME":3000,
              'IMAGE':{0:pygame.image.load('Images/ninja.png'), 1:pygame.image.load('Images/ninja1.png')}},
            "Big_Hero" :{
               "DAMAGE_RATE":30 ,
               "SPEED_RATE":40,
               "HEALTH":100,
               "BULLET":"Sword",
               "LOADTIME":3000,
                'IMAGE':{0:pygame.image.load('Images/Big_Hero.gif'), 1:pygame.image.load('Images/Big_Hero1.gif')}},
            "Zombie" :{
           "DAMAGE_RATE":20 ,
           "SPEED_RATE":80,
           "HEALTH":30,
           "BULLET":"TOF",
           "LOADTIME":200,
            'IMAGE':{0:pygame.image.load('Images/zombie.png'), 1:pygame.image.load('Images/zombie1.png')}},
             "Soldier76" :{
           "DAMAGE_RATE":10 ,
           "SPEED_RATE":20,
           "HEALTH":30,
           "BULLET":"Gun",
           "LOADTIME":7000,
            'IMAGE':{0:pygame.image.load('Images/soldier76.png'), 1:pygame.image.load('Images/soldier761.png')}},
            "Big_Tower" :{
                "DAMAGE_RATE":90 ,
                "SPEED_RATE":10,
                "HEALTH":500,
                "BULLET":"TowerSword",
                "LOADTIME":1000000,
                'IMAGE':{0:pygame.image.load('Images/tall_tower.png'), 1:pygame.image.load('Images/tall_tower.png')}},
            "Small_Tower" :{
                "DAMAGE_RATE":90 ,
                "SPEED_RATE":10,
                "HEALTH":250,
                "BULLET":"TowerSword",
                "LOADTIME":1000000,
                'IMAGE':{0:pygame.image.load('Images/small_tower.png'), 1:pygame.image.load('Images/small_tower.png')}}
           }

Bullets_Dic={"Sword" : {"DAMAGE" : 40 , "SPEED" : 3 , "RANGE" : 2 },
             "Gun" : {"DAMAGE" : 30 , "SPEED" : 6 , "RANGE" : 4 }, "TowerSword" : {"DAMAGE" : 60 , "SPEED" : 6 , "RANGE" : 8 }
             , "TOF" : {"DAMAGE" : 3 , "SPEED" : 6 , "RANGE" : 4 },
             "KATAN" : {"DAMAGE" : 60 , "SPEED" : 6 , "RANGE" : 4 }}

