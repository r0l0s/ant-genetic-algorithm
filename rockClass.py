import globalSystems
class Rock:
    def __init__(self,row,col,canvas,visual_grid):
        
        self.row = row
        self.col = col
        self.canvas = canvas
        self.id = "rock"
        self.visual_grid = visual_grid
        self.visual_grid[self.row][self.col] = self.id

    def canCross(self):
        return False
