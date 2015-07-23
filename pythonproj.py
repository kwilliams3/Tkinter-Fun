#!/usr/bin/env python3

from tkinter import Tk, Frame, Button, Label, Toplevel, Canvas
import random

class Frame1(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        but = Button(parent, text="New Window",
                     command= lambda: self.newWindow(parent))
        but.pack(expand=True)
        but2 = Button(parent, text="Exit",
                     command=parent.destroy)
        but2.pack(side="bottom")

    def newWindow(self, parent):
        random.seed()
        colorInt = random.randint(0,2)
        if colorInt == 0:
            bgColor = "red"
        elif colorInt == 1:
            bgColor = "white"
        else:
            bgColor = "blue"
        top = Toplevel()
        winWidth, winHeight = 200, 200
        top.minsize(width=winWidth, height=winHeight)
        top.title("New!")
        top.configure(background=bgColor)
        label = Label(top, text=("This window has a " + str(bgColor) +
                                 " background!"))
        label.pack(side="top")
        but = Button(top, text="New Window",
                     command= lambda: self.newWindow(parent))
        but.pack(expand=True)
        but2 = Button(top, text="Close All", command=parent.destroy)
        but2.pack(side="bottom")
        but3 = Button(top, text="Close Current", command=top.destroy)
        but3.pack(side="bottom")
        #square = Square(top)

class Square():
    def __init__(self, parent):
        self.parent = parent
        can = Canvas(parent, width=100, height=100)

def main():
    rootWindow = Tk()
    rootWindow.title("Congratulations!")
    rootWindow.minsize(width=200, height=200)
    rootWindow.configure(background='blue')
    app = Frame1(rootWindow)

    app.mainloop()

if __name__ == "__main__":
    main()
