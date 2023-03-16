from random import *
from tkinter import *
from sys import *
from threading import *
from time import *
from secrets import *

class Case:
    def __init__(self,isSnake,button):
        self.isSnake = isSnake
        self.button = button
        self.nextState = None
        self.isApple = False

class Board:
    def __init__(self,window,width,height,caseSize):
        self.lstCase = []
        self.lstSnake = []
        self.window = window
        self.width = width
        self.height = height
        self.caseSize = caseSize
        self.direction = ""

    def initLst(self):
        for i in range(self.height):
            self.lstCase.append([])

    def initButtonTkinter(self):
        for i in range(self.height):
            for j in range(self.width):
                isSnake = False
                color = "white"
                if (i == int(width/2) and j == int(height/2)):
                    isSnake = True
                    color = "black"
                self.lstCase[i].append(Case(isSnake,self.canvas.create_rectangle(i*self.caseSize,j*self.caseSize,i*self.caseSize + self.caseSize,j*self.caseSize + self.caseSize,fill=color)))
                if (isSnake == True):
                    self.lstSnake.append(self.lstCase[i][j])

    def placeAnApple(self): 
        x = randint(0,self.width-1)
        y = randint(0,self.height-1)
        while self.lstCase[x][y].isSnake == True :
            print(x)
            print(y)
            x = randint(1,self.width-1)
            y = randint(1,self.height-1)

        self.lstCase[x][y].isApple = True
        self.canvas.itemconfig(self.lstCase[x][y].button, fill= "red")

    def initWindow(self):
        self.window.title('jeuDeLaVie')
        self.window.geometry(str(int(self.caseSize*self.width)) + "x" + str(int(self.caseSize*self.height)))
        self.window.bind("<Left>", self.leftArrow)
        self.window.bind("<Right>", self.rightArrow)
        self.window.bind("<Up>", self.upArrow)
        self.window.bind("<Down>", self.downArrow)
        self.window.bind("<Button 1>", self.onClick)

    def initCanvas(self):
        self.canvas = Canvas(height=self.caseSize*self.height, width=self.caseSize*self.width)
        self.canvas.grid(row=0, column=0)

    def onClick(self,event):
        x = event.x
        y = event.y
        for i in range(self.height):
            for j in range(self.width):
                if self.canvas.coords(self.lstCase[i][j].button)[0] < x:
                    if self.canvas.coords(self.lstCase[i][j].button)[1] < y:
                        if self.canvas.coords(self.lstCase[i][j].button)[2] > x:
                            if self.canvas.coords(self.lstCase[i][j].button)[3] > y:
                                if self.lstCase[i][j].isSnake == False:
                                    self.canvas.itemconfig(self.lstCase[i][j].button, fill="black", outline="white")
                                    self.lstCase[i][j].isSnake = True
                                    self.lstSnake.append(self.lstCase[i][j])
                                elif self.lstCase[i][j].isSnake == True:
                                    self.canvas.itemconfig(self.lstCase[i][j].button, fill="white", outline="black")
                                    self.lstCase[i][j].isSnake = False
                                    self.lstSnake.remove(self.lstCase[i][j])
                                return

    def updateState(self,apple):
        if apple == False:
            self.lstSnake[len(self.lstSnake)-1].isSnake = False
            self.canvas.itemconfig(self.lstSnake[len(self.lstSnake)-1].button, fill="white", outline="black")
            self.lstSnake.pop()
        else:
            self.placeAnApple()
    
    def isDead(self):
            for i in range(len(self.lstSnake)-1,-1,-1):
                self.lstSnake[i].isSnake = False
                self.canvas.itemconfig(self.lstSnake[i].button, fill="white", outline="black")
            self.lstSnake.clear()

            self.window.unbind("<Left>")
            self.window.unbind("<Right>")
            self.window.unbind("<Up>")
            self.window.unbind("<Down>")

    def leftArrow(self,event):
        for i in range(self.height):
            for j in range(self.width):
                if i == 0 and self.lstCase[i][j] == self.lstSnake[0]:
                    self.isDead()
                    return
                if (i < self.height-1):
                    if (self.lstCase[i+1][j] == self.lstSnake[0]):
                        self.lstCase[i][j].isSnake = True
                        self.lstSnake.insert(0,self.lstCase[i][j])
                        self.canvas.itemconfig(self.lstCase[i][j].button, fill="black", outline="white")
                        apple = False
                        if self.lstCase[i][j].isApple == True:
                            apple = True
                            self.lstCase[i][j].isApple = False
                        self.updateState(apple)
                        return

    def rightArrow(self,event):
        print(self.height)
        for i in range(self.height):
            for j in range(self.width):
                if i == -1 and self.lstCase[i][j] == self.lstSnake[0]:
                    print(i)
                    self.isDead()
                    return
                if (self.lstCase[i-1][j] == self.lstSnake[0]):
                    self.lstCase[i][j].isSnake = True
                    self.lstSnake.insert(0,self.lstCase[i][j])
                    self.canvas.itemconfig(self.lstCase[i][j].button, fill="black", outline="white")
                    apple = False
                    if self.lstCase[i][j].isApple == True:
                        apple = True
                        self.lstCase[i][j].isApple = False
                    self.updateState(apple)
                    return

    def upArrow(self,event):
        for i in range(self.height):
            for j in range(self.width):
                if j == 0 and self.lstCase[i][j] == self.lstSnake[0]:
                    self.isDead()
                    return
                if (j < self.width-1):
                    if (self.lstCase[i][j+1] == self.lstSnake[0]):
                        self.lstCase[i][j].isSnake = True
                        self.lstSnake.insert(0,self.lstCase[i][j])
                        self.canvas.itemconfig(self.lstCase[i][j].button, fill="black", outline="white")
                        apple = False
                        if self.lstCase[i][j].isApple == True:
                            apple = True
                            self.lstCase[i][j].isApple = False
                        self.updateState(apple)
                        return

    def downArrow(self,event):
        for i in range(self.height):
            for j in range(self.width):
                if j == -1 and self.lstCase[i][j] == self.lstSnake[0]:
                    self.isDead()
                    return
                if (self.lstCase[i][j-1] == self.lstSnake[0]):
                    self.lstCase[i][j].isSnake = True
                    self.lstSnake.insert(0,self.lstCase[i][j])
                    self.canvas.itemconfig(self.lstCase[i][j].button, fill="black", outline="white")
                    apple = False
                    if self.lstCase[i][j].isApple == True:
                        apple = True
                        self.lstCase[i][j].isApple = False
                    self.updateState(apple)
                    return


caseSize = 24
width = 25 #int(input("nb de lignes"))
height = 25 #int(input("nb de colones"))
window=Tk()

board = Board(window,width,height,caseSize)
board.initLst()
board.initCanvas()
board.initButtonTkinter()
board.placeAnApple()
board.initWindow()
board.window.mainloop()
