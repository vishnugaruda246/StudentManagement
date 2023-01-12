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
    

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=0,relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2,command=self.AddStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2,command = self.GetAdmission_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, command=self.GetAdmission_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, command=self.ClearScreen ,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, command=self.Exit ,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=340,width=100)

#Adding student details
    def AddStudent(self):
        self.ClearScreen()
        self.admission = Label(self.frame_1,text='Admission number',font=(self.font_2, 15, "bold")).place(x=40,y=30)
        self.admission_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.admission_entry.place(x=40,y=60, width=200)

        self.name = Label(self.frame_1, text="Full Name", font=(self.font_2, 15, "bold")).place(x=300,y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=300,y=60, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold")).place(x=40,y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=40,y=130, width=200)

        self.subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold")).place(x=300,y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.place(x=300,y=130, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold")).place(x=40,y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=40,y=200, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold")).place(x=300,y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=300,y=200, width=200)
        
        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold")).place(x=40,y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40,y=270, width=200)

        self.dob = Label(self.frame_1, text="Date of birth", font=(self.font_2, 15, "bold")).place(x=300,y=240)
        self.dob_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.dob_entry.place(x=300,y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold")).place(x=40,y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40,y=340, width=200)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold")).place(x=300,y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300,y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=200,y=389,width=100)
    
    def Submit(self):
        if self.name_entry.get() == "" or self.admission_entry.get() == "" or self.name_entry.get() == "" or self.course_entry.get() == "" or self.subject_entry.get() == "" or self.year_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.dob_entry.get() == "" or self.contact_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.admission_entry.get())
                row=curs.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The contact number is already exists, please try again with another number",parent=self.window)
                else:
                    curs.execute("insert into student (admission_no,name,course,subject,year,age,gender,dob,contact,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                            self.admission_entry.get(),
                                            self.name_entry.get(),
                                            self.course_entry.get(),
                                            self.subject_entry.get(),
                                            self.year_entry.get(),
                                            self.age_entry.get(),
                                            self.gender_entry.get(),
                                            self.dob_entry.get(),
                                            self.contact_entry.get(),
                                            self.email_entry.get()  
                                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
#displaying student details
    def GetContact_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"), bg=self.color_1).place(x=140,y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=150,width=80)
            
    def CheckContact_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row=curs.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Contact number doesn't exists",parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.admission_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.subject_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.dob_entry .delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()