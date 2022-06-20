class Wall:
    "Abstraction of the barrier in the game"
    def __init__(self, x, y, orient):
        """(x,y) is the coordinate of the left or lower point of the wall, and orient is the orientation of the wall, which is either 'h'(horizontal) or 'v'(vertical)"""
        self.x = x
        self.y = y
        self.orient = orient

class Player:
    """Abstraction of one player"""
    def __init__(self, id, x, y, num_remain_walls):
        self.id = id
        self.x = x
        self.y = y
        self.num_remain_walls = num_remain_walls
    
    
    
class Board:
    """Contain all information about the board"""
    def __init__(self):
        self.walls = []
        self.players = []

