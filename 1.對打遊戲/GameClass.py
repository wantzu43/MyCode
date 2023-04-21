# -*- coding: utf-8 -*-
"""
2023/01/17 汪汪隊對打遊戲撰寫
"""
import random
import datetime

class Role:
    global RoleName,SkillList,Team,FireTeam
    Team =  {}
    FireTeam = {}
    RoleName = ['阿奇','毛毛','天天','灰灰','小礫','路馬']
    SkillList = {'超級火焰':'25','無敵大砲':'25','水槍射擊':'30','泰山壓頂':'30','花粉攻擊':'20','臭氣沖天':'20'}
   
    #產生角色
    def __init__(self):
        self.name = random.choice(RoleName)  #角色名稱
        self.HP = random.randrange(100,130,5) #血量隨機
        self.Attack = random.randrange(5,10,1) #普通攻擊傷害
        self.Skillkey,self.Skillval = random.choice(list(SkillList.items())) #必殺技能
        
    #抽卡分隊    
    def DrewCard(self,name):
        for i in range(3):
            print('\n' + name + '的第' + str(i+1) + '位角色:') 
            role = Role() #產生角色
            print('名稱:' + role.name)
            print('血量:' + str(role.HP))
            print('普通攻擊傷害:' + str(role.Attack))
            print('必殺技:「' + str(role.Skillkey) + '」，傷害為:' + str(role.Skillval))
            RoleName.remove(role.name)
            SkillList.pop(role.Skillkey)
            if name == "你":
                Team[i] = role
            else:
                FireTeam[i] = role
        if name == "你":
            return Team
        else:
            return FireTeam
        
class Game:
    global Teamdt
    global FireTeamdt
    Teamdt = datetime.datetime.now()
    FireTeamdt = datetime.datetime.now()
    
    #猜拳決定攻擊先後順序
    def Mora(self):
        print('\n來猜拳決定誰先攻擊吧!')
        fingerdict = {'1':'剪刀','2':'石頭','3':'布'}
        ran = ['1','2','3']
        finger = ['剪刀','石頭','布']
        result = 0
        while result == 0:
            print('=============================')
            req = input('(1)剪刀、(2)石頭、(3)布選一個出吧!:')
            firereq = random.choice(finger)
            if (req in ran) or (req in finger):
                if (req in ran):
                    req = fingerdict[req]
                print('\n你出的拳是:' + req)
                print('對手出的拳是:' + firereq + '\n')
            
                if req == firereq :
                    print('平手，再來一次')
                elif (req == '剪刀' and firereq == '布') or (req == '石頭' and firereq == '剪刀') or (req == '布' and firereq == '石頭') :
                    input('你贏了，你先發動攻擊吧!')
                    result = 1
                else:
                    input('你輸了，對手先攻擊囉!')
                    result = 2
            else:
                print('不要調皮，請出正常的拳!')
        return result
    
    #執行必殺技
    def ExecuteSkill(self,who,lastdt,i):
        global Teamdt
        global FireTeamdt
        if i == 2:    
            print('發動必殺技!')
            if who == 1:
                Teamdt = datetime.datetime.now()
            else:
                FireTeamdt = datetime.datetime.now()
            return True
        else:
            if who == 1 and float((lastdt - Teamdt).total_seconds()) >= float(10):
                print('體力已恢復，可以再次必殺技了!')
                Teamdt = lastdt
                return True
            elif who == 2 and float((lastdt - FireTeamdt).total_seconds()) >= float(10):
                print('體力已恢復，可以再次必殺技了!')
                FireTeamdt = lastdt
                return True
            else:
                print('體力尚未恢復，必殺技還不能使用!')
                return False
            
        
        
        
            
            
        

    
    


        