import tkinter as tk
import arithmetic as art # import new class everytime you created a new file you want to use
from graphics import *
import random

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=500)
blackLine = canvas.create_line(10, 10, 50, 200)
moveX = 240

class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.minsize(width=300, height=200)
        self.master.config()

        canvas.pack()


        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>',self.right_key)


        self.main_frame = tk.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

    # def main()
    #     win = GraphWin("graphics window", 500, 300)



    def draw_black_line():
        # blackLine = canvas.create_line(10, 10, 50, 200)
        canvas.delete(ALL)

    @staticmethod
    def left_key(event):
        result = art.Arithmetic.addition(43, 10)
        #draw_black_line()
        global moveX
        i = 240
        randNumb = random.randint(0, 5)
        global blackLine
        if (randNumb == 3):
            while i > 230:
                redLine = canvas.create_line(50, 50, moveX, 270, fill='red')
                moveX -= 1
                i -= 1
        if (randNumb == 5):
            while i > 230:
                blueLine = canvas.create_line(50, 50, moveX, 270, fill='blue')
                moveX -= 1
                i -= 1
        if (randNumb == 2):
            while i > 230:
                blackLine = canvas.create_line(50, 50, moveX, 270, fill='black')
                moveX -= 1
                i -= 1
        if (randNumb == 0):
            while i > 230:
                yellowLine = canvas.create_line(50, 50, moveX, 270, fill='yellow')
                moveX -= 1
                i -= 1
        if (randNumb == 1):
            while i > 230:
                greenLine = canvas.create_line(50, 50, moveX, 270, fill='green')
                moveX -= 1
                i -= 1
        if (randNumb == 4):
            while i > 230:
                purpleLine = canvas.create_line(50, 50, moveX, 270, fill='purple')
                moveX -= 1
                i -= 1
        #canvas.delete(blackLine)
        canvas.after(1000, canvas.delete, blackLine)
        print (str(result) + " left key pressed")

    @staticmethod
    def right_key(event):
        result = art.Arithmetic.division(43, 10)
        i = 240
        randNumb = random.randint(0, 5)
        global moveX
        if(randNumb == 3):
            while i < 250:
                redLine = canvas.create_line(50, 50, moveX, 270, fill='red')
                moveX += 1
                i += 1
        if(randNumb == 5):
            while i < 250:
                blueLine = canvas.create_line(50, 50, moveX, 270, fill='blue')
                moveX += 1
                i += 1
        if(randNumb == 2):
            while i < 250:
                blackLine = canvas.create_line(50, 50, moveX, 270, fill='black')
                moveX += 1
                i += 1
        if(randNumb == 0):
            while i < 250:
                yellowLine = canvas.create_line(50, 50, moveX, 270, fill='yellow')
                moveX += 1
                i += 1
        if(randNumb == 1):
            while i < 250:
                greenLine = canvas.create_line(50, 50, moveX, 270, fill='green')
                moveX += 1
                i += 1
        if (randNumb == 4):
            while i < 250:
                purpleLine = canvas.create_line(50, 50, moveX, 270, fill='purple')
                moveX += 1
                i += 1
        #canvas.delete("all")
        moveX += 1
        print(random.randint(0, 5))
        print (str(result) + " key pressed")




xUnit = 200
app = Application(root)

app.mainloop()
