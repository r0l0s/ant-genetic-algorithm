from tkinter import *
import copy
import antClass
import airClass
import rockClass
import sugarClass
import wineClass
import poisonClass
import exitClass
import globalSystems
import time
import threading



# Maze Editor Class
class MazeRunner:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Maze Creator")
        
        # Default settings
        self.cell_size = globalSystems.cell_size
        self.maze_size = globalSystems.maze_size
        self.current_mode = 1  # Default mode: wall
        
        self.grid = [[None] * self.maze_size for _ in range(self.maze_size)]
        self.cell_grid = [[None] * self.maze_size for _ in range(self.maze_size)]
        self.visual_grid = [[None] * self.maze_size for _ in range(self.maze_size)]
    
        
        # Grid and color mappings
        self.colors = {
            "air":"white",
            "rock":"black",
            "sugar":"#22d3ee",
            "wine":"#4c0519",
            "poison":"#84cc16",
            "exit":"#fbbf24"
            }
        
        # Set up the canvas
        self.canvas = Canvas(root, width=self.cell_size*self.maze_size,
                                height=self.cell_size*self.maze_size, bg="#71717a")
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        
        self.antHealth = Label(self.root, text="")
        self.antHealth.place(relx=0.1, rely=0.2, anchor="center")

        self.antAlcohol = Label(self.root, text="")
        self.antAlcohol.place(relx=0.1, rely=0.3, anchor="center")

        self.antScore = Label(self.root, text="")
        self.antScore.place(relx=0.1, rely=0.4, anchor="center")

        self.genertaion = Label(self.root, text="")
        self.genertaion.place(relx=0.1, rely=0.5, anchor="center")


        self.setup()

    def setGrid(self):
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                self.visual_grid[row][col] = copy.copy(globalSystems.visual_grid[row][col])
                if globalSystems.grid[row][col] == 0:
                    self.grid[row][col] = airClass.Air(row,col,self.canvas,self.visual_grid)
                elif globalSystems.grid[row][col] == 1:
                    self.grid[row][col] = rockClass.Rock(row,col,self.canvas,self.visual_grid)
                elif globalSystems.grid[row][col] == 2:
                    self.grid[row][col] = sugarClass.Sugar(row,col,self.canvas,self.visual_grid)
                elif globalSystems.grid[row][col] == 3:
                    self.grid[row][col] = wineClass.Wine(row,col,self.canvas,self.visual_grid)
                elif globalSystems.grid[row][col] == 4:
                    self.grid[row][col] = poisonClass.Poison(row,col,self.canvas,self.visual_grid)
                elif globalSystems.grid[row][col] == 5:
                    self.grid[row][col] = exitClass.Exit(row,col,self.canvas,self.visual_grid)
                

    def setup(self):
        self.create_grid()
        self.setGrid()
        globalSystems.ant.setCanvas(self.canvas)
        globalSystems.ant.respawnEntity()
        globalSystems.ant.setGrid(self.grid)
        globalSystems.ant.setVisual_Grid(self.visual_grid)
        self.update_cell()

    def restart(self):
        globalSystems.ant.destroyEntity()
        self.setGrid()
        globalSystems.ant.respawnEntity()
        globalSystems.ant.printPosition()
        #globalSystems.ant.setGrid(self.grid)
        globalSystems.ant.setVisual_Grid(self.visual_grid)
        self.update_cell()


    def create_grid(self):
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                x1, y1 = col*self.cell_size, row*self.cell_size
                x2, y2 = x1+self.cell_size, y1+self.cell_size
                self.cell_grid[row][col] = (self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black"))

                
        
    def update_cell(self):
        """Updates the color of a cell based on its type."""
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                cell_type = self.visual_grid[row][col]
                self.canvas.itemconfig(self.cell_grid[row][col], fill=self.colors[cell_type], outline="black")

    
    def goEat(self):

        globalSystems.ant.eat()

        self.update_cell()



    def startLoop(self):
        
        globalSystems.ant.geneticAlgorithm()
        visual = threading.Thread(target=globalSystems.plot.runPlot)
        visual.daemon = True
        visual.start()
        
        while True:
            
            if globalSystems.ant.getGenome() == False:
                self.restart()
            
            self.antHealth["text"] = f"Health: {globalSystems.ant.getHealth()}"
            self.antAlcohol["text"] = f"Alcohol: {globalSystems.ant.getAlcohol()}"
            self.antScore["text"] = f"Score: {globalSystems.ant.getScore()}"
            self.genertaion["text"] = f"Generation: {globalSystems.ant.getGen()}"
            self.update_cell()
            time.sleep(0.05)
            






def EditorWindow():
    
    window = Tk()
    window.minsize(width= 800, height=700)
    window.title("Maze Configure")
    window.configure(bg="#262626")
    
    # Run the Tkinter event loop
    maze_runner = MazeRunner(window)

    testing = threading.Thread(target= lambda: maze_runner.startLoop())
    testing.daemon = True


    # Butons
    actionA_button = Button(window, text="Move Up", width=15, height=2, command= globalSystems.ant.moveUp)
    actionA_button.place(relx=0.9, rely=0.2, anchor="center")

    actionB_button = Button(window, text="Move Down", width=15, height=2, command= globalSystems.ant.moveDown)
    actionB_button.place(relx=0.9, rely=0.3, anchor="center")

    actionC_button = Button(window, text="Move Right", width=15, height=2, command= globalSystems.ant.moveRight)
    actionC_button.place(relx=0.9, rely=0.4, anchor="center")

    actionD_button = Button(window, text="Move Left", width=15, height=2, command= globalSystems.ant.moveLeft)
    actionD_button.place(relx=0.9, rely=0.5, anchor="center")

    actionD_button = Button(window, text="Eat", width=15, height=2, command= maze_runner.goEat)
    actionD_button.place(relx=0.9, rely=0.6, anchor="center")

    actionE_button = Button(window, text="Restart", width=15, height=2, command= maze_runner.restart)
    actionE_button.place(relx=0.9, rely=0.7, anchor="center")

    actionF_button = Button(window, text="Actions", width=15, height=2, command= testing.start)
    actionF_button.place(relx=0.9, rely=0.8, anchor="center")
        
    window.mainloop()
