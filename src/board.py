'''
This file contains:
Board creation,
Handicap setup,
Game logic (like capture and ko)
Player info.
'''

from random import randint

class Board:

    def __init__(self, size):
        self.size = size

    def createBoard(self):
        '''
        Creates two dimensional list.
        '''
        board = [['' for cell in range(0,self.size)] for row in range(0,self.size)]
        return board

class Stone:

    def __init__(self, x,y,player):
        self.pos_x = x
        self.pos_y = y
        self.player = player

class Player:

    def __init__(self,color,name,rank):
        self.color = color
        self.name = name
        self.rank = rank
