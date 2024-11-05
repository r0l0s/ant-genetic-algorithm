
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading

plt.style.use('fivethirtyeight')

class Plot:
    def __init__(self):
        
        self.x_vals = []
        self.y_vals = []
        self.index = count()

    def setVals(self, generation, time ):
        self.x_vals.append(generation)
        self.y_vals.append(time)
        


    def animate(self,i):
        plt.cla()
        plt.plot(self.x_vals, self.y_vals)


    def runPlot(self):
        anim = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        plt.tight_layout()
        plt.show()
