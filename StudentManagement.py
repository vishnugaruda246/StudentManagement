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
        self.frame_1 = Frame(self.window)
        self.frame_1.place(x=0, y=0, width=540, relheight = 1)
        photo = PhotoImage(file="vivid.png")
        label = Label(self.frame_1, image=photo)
        label.image = photo
        label.pack()
        label.place(x=0, y=0)
    

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2,command=self.AddStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2,  cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=340,width=100)

    def AddStudent(self):
        self.admission = Label(self.frame_1,text='Admission number',font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.admission_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.admission_entry.place(x=40,y=60, width=200)

        self.name = Label(self.frame_1, text="Full Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=300,y=60, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=40,y=130, width=200)

        self.subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.place(x=300,y=130, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=40,y=200, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=300,y=200, width=200)
        
        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40,y=270, width=200)
        
        self.dob = Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.dob_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dob_entry.place(x=300,y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40,y=340, width=200)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300,y=340, width=200)
    

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()