#!/usr/bin/env python3

from tkinter import Tk, Frame, Button, Label, Toplevel, Canvas
import random

class Frame1(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        but = Button(parent, text="New Window", command=self.newWindow)
        but.place(relx=0.25, rely=0.5)

    def newWindow(self):
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
        but = Button(top, text="New Window", command=self.newWindow)
        but.place(relx=0.25, rely=0.5)
        label = Label(top, text=("This window has a " + str(bgColor) +
                                 " background!"))
        label.pack(side="top")
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
