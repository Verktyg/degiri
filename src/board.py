from random import randint

class Board:

    def __init__(self, size):
        self.size = size

class Stone:

    def __init__(self, x,y,player):
        self.pos_x = x
        self.pos_y = y
        self.player = player

class Rules:
    
    def __init__(self,ruleset,time,handicap,komi):
        self.ruleset = ruleset
        self.time = time
        self.handicap = handicap
        self.komi = komi

class Player:

    def __init__(self,color,name,rank):
        self.color = color
        self.name = name
        self.rank = rank
