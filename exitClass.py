import globalSystems
class Exit:
    def __init__(self,row,col,canvas, visual_grid):
        
        self.row = row
        self.col = col
        self.canvas = canvas
        self.entity = None
        self.id = "exit"
        self.visual_grid = visual_grid
        self.visual_grid[self.row][self.col] = self.id

    def createEntity(self):
        x1, y1 = self.col * 40, self.row * 40
        x2, y2 = x1 + 40, y1 + 40
        self.entity = self.canvas.create_rectangle(x1, y1, x2, y2, fill="#fbbf24", outline="black")

    def destroyEntity(self):
        self.canvas.delete(self.entity)
