# -*- coding: utf-8 -*-
"""
2023/01/17 汪汪隊對打遊戲撰寫
"""
import random
import datetime
from GameClass import Role
from GameClass import Game

if __name__ == "__main__":
    global Team
    global FireTeam
    
    print('歡迎來到「汪汪隊對打遊戲」!')
    req = input('讓我們開始遊戲吧?(Y/N):')
    
    if req.upper() == "Y" :
        r1 = input('那就先來抽角色吧!(go/bye):') 
        
        if r1.lower() == "go":
            Team = Role().DrewCard("你")
            r2 = input('\n來看看你的對手是哪些角色吧!(OK/No):')
            
            if r2.upper() == "OK":
                FireTeam = Role().DrewCard("對手")
                
                r3 = input('\n那就開始決鬥吧!(OK/No):')
                if r3.upper() == "OK":
                    whofirst = Game().Mora()
                    i = 1
                    k = 0
                    index = [0,1,2]
                    WF = "未有勝負"
                    #開始對決
                    while (Team[0].HP != 0 or Team[1].HP != 0 or Team[2].HP != 0) and (FireTeam[0].HP != 0 or FireTeam[1].HP != 0 or FireTeam[2].HP != 0):
                        
                        if k % 2 == 0:
                            print('\n============第' + str(i)+ '回合開始============\n')
                        v = random.choice(index) #隨機派出一位角色
                        att = 0 #存普通攻擊傷害或必殺技傷害
                        IsOK = False #是否能發動必殺技
                        if i >= 2 : #第二回合開始才能發動必殺技
                            IsOK = Game().ExecuteSkill(whofirst,datetime.datetime.now(),i) #判斷是否過5秒鐘，是否發動攻擊
                            
                        if whofirst == 1: #你的戰隊先攻擊
                            if Team[v].HP == 0:
                                index.remove(v)
                                v = random.choice(index)
                            if IsOK == True:
                                att = Team[v].Skillval
                                print('你的角色:' + Team[v].name + '發動了必殺技攻擊「' + Team[v].Skillkey + '」，傷害為:' + str(att))
                            else:  
                                att = Team[v].Attack
                                print('你的角色:' + Team[v].name + '發動了普通攻擊，傷害為:' + str(att))
                            dead = 0
                            for j in range(3):
                                if FireTeam[j].HP != 0 :
                                    if FireTeam[j].HP <= int(att):
                                        FireTeam[j].HP = 0
                                        print('對手: ' + FireTeam[j].name + '的血量剩餘:' + str(FireTeam[j].HP) + '，已陣亡!')
                                        dead +=1
                                    else:
                                        FireTeam[j].HP = FireTeam[j].HP - int(att)
                                        print('對手: ' + FireTeam[j].name + '的血量剩餘:' + str(FireTeam[j].HP))
                                else:
                                    print('對手: ' + FireTeam[j].name + '的血量剩餘:' + str(FireTeam[j].HP) + '，已陣亡!')
                                    dead +=1
                            if dead == 3:
                                print('\n對手的全部角色都已陣亡，你贏了!!!')
                                WF = "已有勝負"
                            whofirst = 2
                            k+=1    
                            
                        elif whofirst == 2: #對手的戰隊先攻擊
                            if FireTeam[v].HP ==  0:
                                index.remove(v)
                                v = random.choice(index)
                            if IsOK == True:
                                att = FireTeam[v].Skillval
                                print('對手的角色:' + FireTeam[v].name + '發動了必殺技攻擊「' + FireTeam[v].Skillkey + '」，傷害為:' + str(att))
                            else:  
                                att = FireTeam[v].Attack
                                print('對手的角色:' + FireTeam[v].name + '發動了普通攻擊，傷害為:' + str(att))
                            
                            dead = 0    
                            for j in range(3):
                                if Team[j].HP != 0 :
                                    if Team[j].HP <= int(att):
                                        Team[j].HP = 0
                                        print('你: ' + Team[j].name + '的血量剩餘:' + str(Team[j].HP) + '，已陣亡!')
                                        dead +=1
                                    else:
                                        Team[j].HP = Team[j].HP - int(att)
                                        print('你: ' + Team[j].name + '的血量剩餘:' + str(Team[j].HP))
                                else:
                                    print('你: ' + Team[j].name + '的血量剩餘:' + str(Team[j].HP) + '，已陣亡!')
                                    dead +=1
                            if dead == 3:
                                print('\n你的全部角色都已陣亡，你輸了!')
                                WF = "已有勝負"
                            whofirst = 1
                            k+=1
                        
                        if (k % 2 == 0) and WF == "未有勝負":
                            input('\n============第' + str(i) + '回合結束============')
                            whofirst = Game().Mora()
                            i+=1
                        elif (k % 2 == 1) and WF == "未有勝負":
                            print('\n==============攻守交換=============\n')
                        if k == 2:    
                            input('\n第二回合可以開始使用必殺技了!')
                        
            elif r2.upper() == "NO":
                print('你害怕了嗎!?')
            else:
                print('好吧，再見!')
            
        elif r1.lower() == "bye":
            print('好吧，再見!')
        else:
            print('有什麼話待會再說吧!')
    else:
        print('謝謝，再見!')