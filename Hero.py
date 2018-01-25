import Data,Bullet
import queue as Q

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
class Node:
    def __init__(self,x,y,p,d_):
        self.x=x
        self.y=y
        self.parent=p
        self.d=d_

def isValid(grid,y,x):
    if y<0 or y>=grid.height:
        return False
    if x<0 or x>=grid.width:
        return False
    return True
    # ham az nazar inke az jadval kharej nashe ham az nezar in ke khali bashe dige


def findTarget(grid,hero):
    g=grid.mat
    checked = []
    side=hero.side
    dy=[0,0,-1,1]
    dx=[-1,1,0,0]
    queue = Q.Queue()
    queue.put(Node(hero.position_x, hero.position_y,None,0))
    checked.append((hero.position_x, hero.position_y))

    while queue.qsize() != 0:
        node = queue.get()

        for i in range(4):
            if (isValid(grid,node.y+dy[i],node.x+dx[i]) and (node.x+dx[i] , node.y+dy[i]) not in checked):
                if (type(g[node.y+dy[i]][node.x+dx[i]])==Hero and g[node.y+dy[i]][node.x+dx[i]].side != side):
                    
                    target = Node(node.x+dx[i],node.y+dy[i],node,node.d+1)
                    return target
                if g[node.y+dy[i]][node.x + dx[i]] == 0:
                    queue.put(Node(node.x + dx[i],node.y + dy[i],node,node.d+1))

                    checked.append((node.x+dx[i],node.y+dy[i]))

    return None
    #ta inja nazdik tarin target malom shode


def nextPosition(hero,target,range):
    if target != None:
        
        if target.d > range:
            while target.parent.parent != None:
                target=target.parent

            hero.position_x = target.x
            hero.position_y = target.y







def herosProcess(grid,currentHeros,currentBullets,cnt):
    for heros in currentHeros:
        for hero in heros:
            damageRange = Data.Bullets_Dic[hero.bullet]["RANGE"]
            if cnt % hero.speed_Rate == 0:
                target = findTarget(grid,hero)
                nextPosition(hero , target , damageRange)
                # bayad hero.nextPostion() bashe

            if cnt % hero.damage_Rate == 0:
                target = findTarget(grid,hero)
                if target!=None:
                    if target.d <= damageRange:
                        (x1,y1)=grid.getPixelByCell(hero.position_x , hero.position_y )
                        (x2,y2)=grid.getPixelByCell(target.x,target.y)
                        newBullet = Bullet.Bullet(x1 , y1 , x2 ,y2 ,hero.bullet,hero.side) # bayad dorost hesabi mosahkhs she in example e
                        currentBullets.append(newBullet)





            

    


    
'''
    REQUIERFD:
    
        SPEED
        POSITION
        HEALTH
        DAMAGE_RATE
        DAMAGE_TYPE        



'''
