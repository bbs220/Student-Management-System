from functools import partial
from tkinter import * # type: ignore
from tkinter import messagebox
import pymysql # type: ignore


# the following commands are used to setup the data structure in MySQL app

# commands for db, run these in the mysql terminal

# create database student_management;
# use student_management;

"""create table student_register(
	f_name VARCHAR(50) NOT NULL,
	l_name VARCHAR(50) NOT NULL,
	course VARCHAR(30) NOT NULL,
	subject VARCHAR(50) NOT NULL,
	year Int(10) NOT NULL,
	age Int(10) NOT NULL,
	gender char(10) NOT NULL,
	birth DATE NOT NULL,
	contact VARCHAR(15) NOT NULL,
	email VARCHAR(100) NOT NULL,
	PRIMARY KEY ( contact )
);"""

"""example  abc_fn       abc_ln
            abc_cou      abc_sub
            1000_yr      1_age
            abc_gen      1990/2/2_birth
            123_con      abc_mail"""

host = 'localhost'
user = 'root'
password = 'root2'
database = 'student_management'

color_1 = "lightblue"
color_2 = "white"
color_3 = "black"
color_4 = "grey"
font_1 = "Bahnschrift Semibold"
font_2 = "Agency FB"


class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("810x480")
        self.window.config(bg="white")

        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4
        self.font_1 = font_1
        self.font_2 = font_2

        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight=1)

        self.frame_2 = Frame(self.window, bg=self.color_2)
        self.frame_2.place(x=540, y=0, relwidth=1, relheight=1)

        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 16), bd=2, command=self.AddStudent,
                             cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=40, width=140)
        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 16), bd=2,
                              command=self.GetContact_View, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=100, width=140)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 16), bd=2,
                                command=self.GetContact_Update, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=160, width=140)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 16), bd=2,
                                command=self.GetContact_Delete, cursor="hand2", bg=self.color_2, fg=self.color_3).place(
            x=68, y=220, width=140)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 16), bd=2, command=self.ClearScreen,
                               cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=280, width=140)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 16), bd=2, command=self.Exit,
                              cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=68, y=340, width=140)

    def AddStudent(self):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=40, y=60, width=200)

        self.surname = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=30)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=300, y=60, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=40, y=130, width=200)

        self.subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                  y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.place(x=300, y=130, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=40, y=200, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=300, y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40, y=270, width=200)

        self.birth = Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                 y=240)
        self.birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.birth_entry.place(x=300, y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40, y=340, width=200)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                              y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300, y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 16), bd=2, command=self.Submit,
                                  cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=200, y=389, width=140)

    def GetContact_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 16), bd=2,
                                  command=self.CheckContact_View, cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=190, y=150, width=140)

    def GetContact_Update(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 16), bd=2,
                                  command=self.CheckContact_Update, cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=190, y=150, width=140)

    def GetContact_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Phone Number", font=(self.font_2, 18, "bold"),
                             bg=self.color_1).place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 16), bd=2, command=self.DeleteData,
                                  cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=190, y=150, width=140)

    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    def Exit(self):
        self.window.destroy()

    def CheckContact_View(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Contact number doesn't exists", parent=self.window)
                else:
                    self.ShowDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def CheckContact_Update(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Contact number doesn't exists", parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    connection.close()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def DeleteData(self):
        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your contact number", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.getInfo_entry.get())
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "Contact number doesn't exist", parent=self.window)
                else:
                    curs.execute("delete from student_register where contact=%s", self.getInfo_entry.get())
                    connection.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    connection.close()
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def GetUpdateDetails(self, row):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                  y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.insert(0, row[0])
        self.name_entry.place(x=40, y=60, width=200)

        self.surname = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(
            x=300, y=30)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.insert(0, row[1])
        self.surname_entry.place(x=300, y=60, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.insert(0, row[2])
        self.course_entry.place(x=40, y=130, width=200)

        self.subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                  y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.insert(0, row[3])
        self.subject_entry.place(x=300, y=130, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.insert(0, row[4])
        self.year_entry.place(x=40, y=200, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.insert(0, row[5])
        self.age_entry.place(x=300, y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                                y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[6])
        self.gender_entry.place(x=40, y=270, width=200)

        self.birth = Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                                 y=240)
        self.birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.birth_entry.insert(0, row[7])
        self.birth_entry.place(x=300, y=270, width=200)

        contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                             y=310)
        contact_data = Label(self.frame_1, text=row[8], font=(self.font_1, 10)).place(x=40, y=340)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                              y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[9])
        self.email_entry.place(x=300, y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2,
                                  command=partial(self.UpdateDetails, row), cursor="hand2", bg=self.color_2,
                                  fg=self.color_3).place(x=160, y=389, width=100)
        self.cancel_bt = Button(self.frame_1, text='Cancel', font=(self.font_1, 12), bd=2, command=self.ClearScreen,
                                cursor="hand2", bg=self.color_2, fg=self.color_3).place(x=280, y=389, width=100)

    def ShowDetails(self, row):
        self.ClearScreen()
        name = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=30)
        name_data = Label(self.frame_1, text=row[0], font=(self.font_1, 10)).place(x=40, y=60)

        surname = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                               y=30)
        surname_data = Label(self.frame_1, text=row[1], font=(self.font_1, 10)).place(x=300, y=60)

        course = Label(self.frame_1, text="Course", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=100)
        course_data = Label(self.frame_1, text=row[2], font=(self.font_1, 10)).place(x=40, y=130)

        subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                             y=100)
        subject_data = Label(self.frame_1, text=row[3], font=(self.font_1, 10)).place(x=300, y=130)

        year = Label(self.frame_1, text="Year", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=170)
        year_data = Label(self.frame_1, text=row[4], font=(self.font_1, 10)).place(x=40, y=200)

        age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=170)
        age_data = Label(self.frame_1, text=row[5], font=(self.font_1, 10)).place(x=300, y=200)

        gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40, y=240)
        gender_data = Label(self.frame_1, text=row[6], font=(self.font_1, 10)).place(x=40, y=270)

        birth = Label(self.frame_1, text="Birthday", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300,
                                                                                                            y=240)
        birth_data = Label(self.frame_1, text=row[7], font=(self.font_1, 10)).place(x=300, y=270)

        contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=40,
                                                                                                             y=310)
        contact_data = Label(self.frame_1, text=row[8], font=(self.font_1, 10)).place(x=40, y=340)

        email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1).place(x=300, y=310)
        email_data = Label(self.frame_1, text=row[9], font=(self.font_1, 10)).place(x=300, y=340)

    def UpdateDetails(self, row):
        if self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or self.subject_entry.get() == "" or self.year_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.birth_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!", " Sorry !, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", row[8])
                row = curs.fetchone()

                if row == None:
                    messagebox.showerror("Error!", "The contact number doesn't exists", parent=self.window)
                else:
                    curs.execute(
                        "update student_register set f_name=%s,l_name=%s, course=%s, subject=%s, year=%s, age=%s, gender=%s, birth=%s, email=%s where contact=%s",
                        (
                            self.name_entry.get(),
                            self.surname_entry.get(),
                            self.course_entry.get(),
                            self.subject_entry.get(),
                            self.year_entry.get(),
                            self.age_entry.get(),
                            self.gender_entry.get(),
                            self.birth_entry.get(),
                            self.email_entry.get(),
                            row[8]
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.ClearScreen()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def Submit(self):
        if self.name_entry.get() == "" or self.surname_entry.get() == "" or self.course_entry.get() == "" or self.subject_entry.get() == "" or self.year_entry.get() == "" or self.age_entry.get() == "" or self.gender_entry.get() == "" or self.birth_entry.get() == "" or self.contact_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!", "Sorry, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                             database=self.database)
                curs = connection.cursor()
                curs.execute("select * from student_register where contact=%s", self.contact_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!",
                                         "The contact number is already exists, please try again with another number",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into student_register (f_name,l_name,course,subject,year,age,gender,birth,contact,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.name_entry.get(),
                            self.surname_entry.get(),
                            self.course_entry.get(),
                            self.subject_entry.get(),
                            self.year_entry.get(),
                            self.age_entry.get(),
                            self.gender_entry.get(),
                            self.birth_entry.get(),
                            self.contact_entry.get(),
                            self.email_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def reset_fields(self):
        self.name_entry.delete(0, END)
        self.surname_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.subject_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.birth_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()
