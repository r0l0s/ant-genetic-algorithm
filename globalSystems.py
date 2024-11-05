import plotClass

maze_size = 10
cell_size = 40

grid_original = None
visual_grid_original = None
cell_grid_original = None

grid = [[None] * maze_size for _ in range(maze_size)]
visual_grid = [[None] * maze_size for _ in range(maze_size)]

ant = None
ant_original_possition = None

plot = plotClass.Plot()