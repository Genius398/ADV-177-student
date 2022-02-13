# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:18:14 2022

@author: Anant
"""

class score2():
    def __init__(self):
        self.__score2=1
        
    def showScore2(self):
        print(self.__score2)
        
    def update_score2(self):
        self.__score2 = self.__score+1
        print(self.__score2)
        
        
player= score2()
player.score2=100
player.update_score2()
player.update_score2()