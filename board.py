
def valid_player_coordinate(x, y):
        """returns True if the player's coordinate is valid, False otherwise"""
        return 0 <= x < 9 and 0 <= y < 9

def valid_wall_coordinate(x, y):
        """returns True if the wall's coordinate is valid, False otherwise"""
        if (x == 0 or x == 9) and (y == 0 or y == 9):
                return False
        else:
            return 0 <= x < 10 and 0 <= y < 10

class Wall:
    "Abstraction of the barrier in the game"
    def __init__(self, x, y, orient):
        """(x1,y1) is the coordinate of the left or lower point of the wall, and orient is the orientation of the wall, which is either 'h'(horizontal) or 'v'(vertical)"""
        self.x1 = x
        self.y1 = y
        self.orient = orient
        self.x2 = x + 1 if orient == 'h' else x
        self.y2 = y + 1 if orient == 'v' else y
        if not valid_wall_coordinate(self.x1, self.y1) or not valid_wall_coordinate(self.x2, self.y2):
            raise ValueError("Invalid wall coordinate")

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
        self.blocked = [[False for i in range(10)] for j in range(10)]

    def add_wall(self, wall):
        if self.blocked[wall.x1][wall.y1] or self.blocked[wall.x2][wall.y2]:
            raise ValueError("Invalid wall coordinate")
        self.walls.append(wall)
        self.blocked[wall.x1][wall.y1] = True
        self.blocked[wall.x2][wall.y2] = True

