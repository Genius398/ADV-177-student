# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:18:40 2022

@author: Anant
"""

class score():
    def __init__(self):
        self.score=1
        
    def showScore(self):
        print(self.score)
        
    def update_score(self):
        self.score = self.score+1
        print(self.score)
        
        
player= score()
player.update_score()
player.update_score()



