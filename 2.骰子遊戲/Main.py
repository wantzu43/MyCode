# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:58:30 2023

@author: 張椀姿
骰子遊戲
"""

from Dice import Game 

if __name__ == "__main__":
    print("歡迎來玩十八仔搏香腸攤")
    req = input("你要(1)付30元買香腸還是(2)要付10元玩十八仔? (請輸入1或2) :")
    if req == "2":
        print("讓我們開始遊戲吧，共五個回合哦!")
        comTotal = 0
        myTotal = 0
        for item in range(5):
            print("===============第" + str(item+1) + "回合===============")
            
            comTotal += Game().ExecuteDice("莊家")
            
            myTotal += Game().ExecuteDice("你")
            
            print("==============第" + str(item+1) + "回合結束=============")
            input("莊家目前累積點數為 : " + str(comTotal) + " 點，你的目前累積點數為 : " + str(myTotal) + " 點")
        if comTotal > myTotal:
            print("非常抱歉!莊家贏了，沒有獲得香腸")
        else:
            print("恭喜!你贏了，獲得一支香腸!")
        
    elif req == "1":
        print("收你三十元給你香腸一支!")
    else:
        print("沒有要買，那謝謝光臨!")
        
        
