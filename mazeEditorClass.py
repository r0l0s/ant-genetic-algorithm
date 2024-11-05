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
import mazeRunner


def startSim(window):
    window.destroy()
    mazeRunner.EditorWindow()


# Maze Editor Class
class MazeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze Creator")
        
        # Default settings
        self.cell_size = globalSystems.cell_size
        self.maze_size = globalSystems.maze_size
        self.current_mode = 1  # Default mode: wall
        
        self.cell_grid = [[None] * self.maze_size for _ in range(self.maze_size)]
        self.grid = [[None] * self.maze_size for _ in range(self.maze_size)]
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

        self.create_grid()
        
        # Draw initial grid
        self.draw_grid()

        self.update_cell()
        
        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        

    def create_grid(self):
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                x1, y1 = col*self.cell_size, row*self.cell_size
                x2, y2 = x1+self.cell_size, y1+self.cell_size

                self.cell_grid[row][col] = (self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black"))

                
        
    
    def draw_grid(self):
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                self.grid[row][col] = airClass.Air(row,col,self.canvas,self.visual_grid)
                globalSystems.grid[row][col] = 0
    
    def on_canvas_click(self, event):
        """Handles cell click based on current drawing mode."""
        row, col = event.y // self.cell_size, event.x // self.cell_size

        if self.current_mode == 0:
            self.grid[row][col] = airClass.Air(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "air"
            self.update_cell()


        if self.current_mode == 1:
            self.grid[row][col] = rockClass.Rock(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "rock"
            self.update_cell()

        if self.current_mode == 2:
            self.grid[row][col] = sugarClass.Sugar(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "sugar"
            self.update_cell()

        if self.current_mode == 3:
            self.grid[row][col] = wineClass.Wine(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "wine"
            self.update_cell()

        if self.current_mode == 4:
            self.grid[row][col] = poisonClass.Poison(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "poison"
            self.update_cell()

        if self.current_mode == 5:
            self.grid[row][col] = exitClass.Exit(row,col,self.canvas,self.visual_grid)
            globalSystems.grid[row][col] = self.current_mode
            globalSystems.visual_grid[row][col] = "exit"
            self.update_cell()
            
        
        if self.current_mode == 6:
            globalSystems.ant = antClass.Ant(row,col,self.canvas)
            globalSystems.ant.createEntity()
            globalSystems.ant.setPosition()
            globalSystems.ant.printPosition()
            self.root.update()
    
    
    def update_cell(self):
        """Updates the color of a cell based on its type."""
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                cell_type = self.visual_grid[row][col]
                self.canvas.itemconfig(self.cell_grid[row][col], fill=self.colors[cell_type], outline="black")
        


    def set_mode(self, mode):
        """Sets the current drawing mode."""
        self.current_mode = mode


def EditorWindow():
    
    window = Tk()
    window.minsize(width= 800, height=700)
    window.title("Maze Configure")
    window.configure(bg="#262626")
    
    # Run the Tkinter event loop
    maze_editor = MazeEditor(window)

    # Butons

    itemA_button = Button(window, text="Air", width=15, height=2, command=lambda: maze_editor.set_mode(0))
    itemA_button.place(relx=0.9, rely=0.2, anchor="center")

    itemB_button = Button(window, text="Rock", width=15, height=2, command=lambda: maze_editor.set_mode(1))
    itemB_button.place(relx=0.9, rely=0.3, anchor="center")

    itemC_button = Button(window, text="Sugar", width=15, height=2, command=lambda: maze_editor.set_mode(2))
    itemC_button.place(relx=0.9, rely=0.4, anchor="center")

    itemD_button = Button(window, text="Wine", width=15, height=2, command=lambda: maze_editor.set_mode(3))
    itemD_button.place(relx=0.9, rely=0.5, anchor="center")

    itemE_button = Button(window, text="Poison", width=15, height=2, command=lambda: maze_editor.set_mode(4))
    itemE_button.place(relx=0.9, rely=0.6, anchor="center")

    itemF_button = Button(window, text="Exit", width=15, height=2, command=lambda: maze_editor.set_mode(5))
    itemF_button.place(relx=0.9, rely=0.7, anchor="center")

    itemG_button = Button(window, text="Ant", width=15, height=2, command=lambda: maze_editor.set_mode(6))
    itemG_button.place(relx=0.9, rely=0.8, anchor="center")

    startButton = Button(window, text="Start", width=30, height=2, command=lambda: startSim(window))
    startButton.place(relx=0.5, rely=0.9, anchor="center")


        
    window.mainloop()
