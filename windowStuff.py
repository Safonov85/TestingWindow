import tkinter as tk
import arithmetic as art # import new class everytime you created a new file you want to use
from graphics import *

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=500)
blackLine = canvas.create_line(10, 10, 50, 200)


class Application(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.minsize(width=300, height=200)
        self.master.config()

        canvas.pack()


        self.master.bind('<Left>', self.left_key)
        self.master.bind('<Right>', self.right_key)


        self.main_frame = tk.Frame()
        self.main_frame.pack(fill='both', expand=True)
        self.pack()

    # def main()
    #     win = GraphWin("graphics window", 500, 300)


    def draw_black_line():
        # blackLine = canvas.create_line(10, 10, 50, 200)
        canvas.delete(blackline)

    @staticmethod
    def left_key(event):
        result = art.Arithmetic.addition(43, 10)
        #draw_black_line()
        canvas.delete(blackLine)
        print (str(result) + " left key pressed")

    @staticmethod
    def right_key(event):
        result = art.Arithmetic.division(43, 10)
        redLine = canvas.create_line(50, 50, 240, 270, fill='red')
        print (str(result) + " key pressed")





app = Application(root)

app.mainloop()
