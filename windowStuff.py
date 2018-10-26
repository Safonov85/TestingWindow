# from Tkinter import *
# from tkinter import *
# import Tkinter
# import tkinter as tk
#
# class Application(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#
# window = tk.Tk()
# window.geometry("300x200")
# window.wm_iconbitmap('bow.ico')
# app = Application(master=window)
# app.mainloop()
from pynput.keyboard import Key, Controller
from graphics import *
import msvcrt

fruits = ['apple', 'banana', 'cherry']

def main():
    # win = GraphWin("My win", 500, 500)
    # win.setBackground(color_rgb(0, 0, 0))
    # point = Point(250, 250)
    # circle = Circle(point, 50)
    # circle.setFill(color_rgb(100, 255, 50))
    # circle.draw(win)

    for x in fruits:
        print(x)
    #point.x += 1

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print(key)


    # win.getMouse()
    # win.close()




def add_to_list():
    fruits.append("orange")

main()