import globalSystems
class Poison:
    def __init__(self,row,col,canvas, visual_grid):
        
        self.row = row
        self.col = col
        self.canvas = canvas
        self.id = "poison"
        self.visual_grid = visual_grid
        self.visual_grid[self.row][self.col] = self.id

    def canCross(self):
        return True
    
    def eat(self):
        globalSystems.ant.setHealth(0)

