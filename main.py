from tkinter import *
import mazeEditorClass
import globalSystems


def openMazeSize(window):
    window.destroy()
    MazeSizeWindow()

def openScores(window):
    window.destroy()
    ScoreWindow()

def openMazeEditor(window, size):
    window.destroy()
    globalSystems.maze_size = size
    mazeEditorClass.EditorWindow()






def MainWindow():
    window = Tk()
    window.minsize(width= 800, height=700)
    window.title("Ant")
    window.configure(bg="#262626")


    ButtonStart = Button(window, text="Start", width=30, height=2, command= lambda: openMazeSize(window))
    ButtonStart.place(relx=0.5, rely=0.25, anchor="center")

    ButtonScore = Button(window, text="Scores",width=30, height=2, command= lambda: openScores(window))
    ButtonScore.place(relx=0.5, rely=0.75, anchor="center")

    window.mainloop()


def MazeSizeWindow():
    window = Tk()
    window.minsize(width= 800, height=700)
    window.title("Ant")
    window.configure(bg="#262626")


    ButtonA = Button(window, text="3 X 3", width=30, height=2, command= lambda: openMazeEditor(window,3))
    ButtonA.place(relx=0.5, rely=0.2, anchor="center")

    ButtonB = Button(window, text="4 X 4", width=30, height=2, command= lambda: openMazeEditor(window,4))
    ButtonB.place(relx=0.5, rely=0.3, anchor="center")

    ButtonC = Button(window, text="5 X 5", width=30, height=2, command= lambda: openMazeEditor(window,5))
    ButtonC.place(relx=0.5, rely=0.4, anchor="center")

    ButtonD = Button(window, text="6 X 6", width=30, height=2, command= lambda: openMazeEditor(window,6))
    ButtonD.place(relx=0.5, rely=0.5, anchor="center")

    ButtonE = Button(window, text="7 X 7", width=30, height=2, command= lambda: openMazeEditor(window,7))
    ButtonE.place(relx=0.5, rely=0.6, anchor="center")

    ButtonF = Button(window, text="8 X 8", width=30, height=2, command= lambda: openMazeEditor(window,8))
    ButtonF.place(relx=0.5, rely=0.7, anchor="center")

    ButtonG = Button(window, text="9 X 9", width=30, height=2, command= lambda: openMazeEditor(window,9))
    ButtonG.place(relx=0.5, rely=0.8, anchor="center")

    ButtonH = Button(window, text="10 X 10", width=30, height=2, command= lambda: openMazeEditor(window,10))
    ButtonH.place(relx=0.5, rely=0.9, anchor="center")


    window.mainloop()


def ScoreWindow():
    window = Tk()
    window.minsize(width= 800, height=700)
    window.title("Ant")
    window.configure(bg="#262626")


    window.mainloop()



MainWindow()

    