# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:19:30 2023

@author: 張椀姿

骰子遊戲
"""

import random

class Game:
    def Dice(self):
        d = list()
        for item in range(4):
            d.append(random.randint(1, 6))
        return d
    
    def ExecuteDice(self, who):
        dice = list()
        isresult = 0
        sam = list()
        
        while isresult == 0:
            dice = Game().Dice()
            print(who + "擲出骰子 : " + str(dice))
            for i in range(1,7):
                if dice.count(i) == 2:
                    dice.remove(i)
                    dice.remove(i)
                    sam.append(i)
                    isresult = 1
                if dice.count(i) == 4:
                    isresult = 1
            if isresult == 0:
                print("沒有結果，再重新擲骰子一次!")
        return Game().GetPoints(who, dice, sam)
            
    def GetPoints(self, who, dice, sam):
        points = 0
        if len(dice) == 4  and len(sam) == 0:
            points = 12
            print("哇，是豹子!")
            
        elif len(dice) == 2:
            points = sum(dice)
            if points == 3:
                print("嘿，是BG!")
                
        elif len(sam) > 1:
            points = max(sam) * 2
            
        print(who + "得 : " + str(points) + " 點")
        return points
        