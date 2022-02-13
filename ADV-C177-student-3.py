# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:18:13 2022

@author: Anant
"""

class score1():
    def __init__(self):
        self.score1=1
        
    def showScore1(self):
        print(self.score1)
        
    def update_score1(self):
        self.score = self.score1+1
        print(self.score1)
        
        
player= score1()
player.score1=100
player.update_score1()
player.update_score1()