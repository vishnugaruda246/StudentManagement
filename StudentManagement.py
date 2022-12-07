from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import Custom as cs
import Credentials as cr
class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("780x480")
        self.window.config(bg = "white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2,  cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2,  cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2,  cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=340,width=100)


root = Tk()
obj = Management(root)
root.mainloop()