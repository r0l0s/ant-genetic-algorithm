import tkinter as tk
import globalSystems
import airClass
import copy
import random
import threading
import time


class Ant:
    def __init__(self, row, col, canvas):
        
        self.row = row
        self.col = col
        self.canvas = canvas
        self.grid = None
        self.entity = None
        self.health = 100
        self.alcohol = 0
        self.score = 0
        self.generation = 0
        self.elapsed_time = 0
        self.genome = False
        self.grid = None
        self.visual_grid = None

    # Ant info
    ##############################################
    def getHealth(self):
        return self.health
    
    def setHealth(self, newHealth):
        self.health = newHealth

    def getAlcohol(self):
        return self.alcohol
    
    def setAlcohol(self):
        self.alcohol += 3

    def getScore(self):
        return self.score
    
    def setScore(self, new):
        self.score += new

    def getGen(self):
        return self.generation
    
    def setGen(self):
        self.generation += 1

    def getElapsedTime(self):
        return self.elapsed_time
    
    def setElapsedTime(self, new_time):
        self.elapsed_time = new_time

    def getGenome(self):
        return self.genome

    def setCanvas(self, new_canvas):
        self.canvas = new_canvas

    def setPosition(self):
        globalSystems.ant_original_possition = copy.copy((self.row,self.col))

    def getPosition(self):
        return globalSystems.ant_original_possition
    
    def printPosition(self):
        print(self.row, self.col)
    
    def setGrid(self, grid):
        self.grid = grid

    def setVisual_Grid(self, visual_grid):
        self.visual_grid = visual_grid

    def moveUp(self):
        new_row = self.row -1
        if new_row < 0:
            print("Out of bounds")
            pass
        else:
            next = self.grid[new_row][self.col]
            if next.canCross():
                self.canvas.move(self.entity, 0,-40)
                self.row = new_row
            else:
                print("Blocked")
                pass

    def moveDown(self):
        new_row = self.row +1
        if new_row > 9:
            print("Out of bounds")
            pass
        else:
            next = self.grid[new_row][self.col]
            if next.canCross():
                self.canvas.move(self.entity, 0,+40)
                self.row = new_row
            else:
                print("Blocked")
                pass

    def moveRight(self):
        new_col = self.col +1
        if new_col > 9:
            print("Out of bounds")
            pass
        else:
            next = self.grid[self.row][new_col]
            if next.canCross():
                self.canvas.move(self.entity, +40,0)
                self.col = new_col
            else:
                print("Blocked")
                pass

    def moveLeft(self):
        new_col = self.col -1
        if new_col < 0:
            print("Out of bounds")
            pass
        else:
            next = self.grid[self.row][new_col]
            if next.canCross():
                self.canvas.move(self.entity, -40,0)
                self.col = new_col
            else:
                print("Blocked")
                pass

    def eat(self):
        
        self.grid[self.row][self.col].eat()
        self.grid[self.row][self.col] = airClass.Air(self.row,self.col,self.canvas,self.visual_grid)

    def destroyEntity(self):
        self.canvas.delete(self.entity)

    
    def createEntity(self):
        x1, y1 = self.col * 40, self.row * 40
        x2, y2 = x1 + 40, y1 + 40
        self.entity = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black")

    def respawnEntity(self):
        self.row = self.getPosition()[0]
        self.col = self.getPosition()[1]
        x1, y1 = self.getPosition()[1] * 40, self.getPosition()[0] * 40
        x2, y2 = x1 + 40, y1 + 40
        self.entity = self.canvas.create_rectangle(x1, y1, x2, y2, fill="red", outline="black")

    def resetValues(self):
        self.health = 100
        self.alcohol = 0
        self.score = 0




    ########################################################################################################################
    ########################################################################################################################
    # Gentic Algorithm
    ########################################################################################################################
    
    def geneticAlgorithm(self):

        actionDic = {
            "mU": self.moveUp,
            "mD": self.moveDown,
            "mR": self.moveRight,
            "mL": self.moveLeft,
            "et": self.eat
        }

        simulation_variables = {
            "total_allels" : 30,
            "group_size" : 12,
            "allele_list" : ["mU","mD","mR","mL","et"],
            "population_list" : []

        }

        for _ in range(simulation_variables["group_size"]):
            genome = [[],None]
            for _ in range(simulation_variables["total_allels"]):
                selection = random.randint(0,4)
                genome[0].append(simulation_variables["allele_list"][selection])
            simulation_variables["population_list"].append(genome)

        
        def running():
            while True:
                start = time.time()
                for genome in simulation_variables["population_list"]:
                    self.genome = True
                    for action in genome[0]:
                        if self.getHealth() == 0:
                            genome[1] = 0
                            self.resetValues()
                            self.genome = False
                            break
                        else:
                            actionDic[action]()
                            time.sleep(0.1)
                    
                    value = self.getScore() - self.getAlcohol()
                    
                    if value < 0:
                        value = 0
                    
                    genome[1] = value
                    self.resetValues()
                    self.genome = False
                    time.sleep(0.1)
                
                self.resetValues()
                self.genome = False
                sorting()
                end = time.time()
                self.setElapsedTime(end-start)
                self.setGen()

                globalSystems.plot.setVals(self.getGen(), self.getElapsedTime())
            
        def sorting(): 
            
            simulation_variables["population_list"].sort(key=lambda x: x[1], reverse=True)
            
            simulation_variables["population_list"] = simulation_variables["population_list"][:len(simulation_variables["population_list"]) //2]
            print(simulation_variables["population_list"] )

            new_population_list = []

            for genome in simulation_variables["population_list"]:
                new_population_list.append(genome[0])
            print(f"new_population_list size: {len(new_population_list)}")
            
            
            new_genome = []

            temp = copy.deepcopy(new_population_list)
            
            for _ in range(len(new_population_list)):

                parents = random.sample(temp,2)

                parent1 = parents[0]
                print(f"parent1 : {parent1}")
                print("")
                
                parent2 = parents[1]
                print(f"parent2 : {parent2}")
                print("")
        
                #temp.remove(random.choice(parents))

                splice1 = parent1[:len(parent1)//2]
                print(f"splice1: {splice1}")
                print("")
                splice2 = parent2[len(parent2)//2:]
                print(f"splice2: {splice2}")
                print("")

                child = splice1+splice2
                
                child[random.randint(0,len(child)-1)] = random.choice(simulation_variables["allele_list"])
                
                print(f"child: {child}")
                print("")
                new_genome.append(child)
            
            
            
            for elements in new_genome:
                new_population_list.append(elements)
            print(f"new_population_list size: {len(new_population_list)}")

            final = []

            for genome in new_population_list:
                final.append([genome,0])

            
            simulation_variables["population_list"] = final

            


            
        
        test = threading.Thread(target= running)
        test.daemon = True
        test.start()



        