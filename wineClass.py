import globalSystems
class Wine:
    def __init__(self,row,col,canvas,visual_grid):
        
        self.row = row
        self.col = col
        self.canvas = canvas
        self.visual_grid = visual_grid
        self.id = "wine"
        self.visual_grid[self.row][self.col] = self.id

    def canCross(self):
        return True
    
    def eat(self):
        if globalSystems.ant.getAlcohol() == 50:
            globalSystems.ant.setHealth(0)
        else:
            globalSystems.ant.setAlcohol()

