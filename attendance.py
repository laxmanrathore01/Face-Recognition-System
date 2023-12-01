from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Student Attendance Details")

        # first image
        img = Image.open("Images/face2.jpg")
        img = img.resize((800,400),Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_label = Label(self.root, image = self.photoImg)
        f_label.place(x=0, y=0, width=800, height=200)


        # second image  
        img1 = Image.open("Images/face2.jpg")
        img1 = img1.resize((800,400),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image = self.photoImg1)
        f_label.place(x=800, y=0, width=800, height=200)


        # background image
        img3 = Image.open("Images/Student.jpeg")
        img3 = img3.resize((1510,710),Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image = self.photoImg3)
        bg_img.place(x=0, y=140, width=1510, height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1510, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=55, width=1480, height=580)

        # ==========Left label Frame==========
        left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_Frame.place(x=10, y=10, width=720, height= 550)

        # left image
        img_left = Image.open("Images/face2.jpg")
        img_left = img_left.resize((720,130),Image.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_label = Label(left_Frame, image = self.photoImg_left)
        f_label.place(x=0, y=0, width=720, height=130)

        # Left inside label and entry
        left_inside_label = LabelFrame(left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        left_inside_label.place(x=5, y=130, width=705, height=370)

        # Attendance Id
        studentId_label = Label(left_inside_label, background="white", text="AttendanceID:", font=("times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        studentId_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        studentId_Entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)


        # Roll No label
        rollNo_label = Label(left_inside_label, background="white", text="Roll No:", font=("times new roman", 12, "bold"))
        rollNo_label.grid(row=0, column=2, padx=10, sticky=W)
        rollNo_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        rollNo_Entry.grid(row=0, column=3, padx=20, pady=5, sticky=W)


        # Student Name Label
        studentName_label = Label(left_inside_label, background="white", text="Student Name:", font=("times new roman", 12, "bold"))
        studentName_label.grid(row=1, column=0, padx=10, sticky=W)
        studentName_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        studentName_Entry.grid(row=1, column=1, padx=20, pady=5, sticky=W)

        # Department Label
        dep_label = Label(left_inside_label, background="white", text="Department:", font=("times new roman", 12, "bold"))
        dep_label.grid(row=1, column=2, padx=10)
        department_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        department_Entry.grid(row=1, column=3, padx=20, pady=5, sticky=W)

        # time label
        time_label = Label(left_inside_label, background="white", text="Time:", font=("times new roman", 12, "bold"))
        time_label.grid(row=2, column=0, padx=10)
        time_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        time_Entry.grid(row=2, column=1, padx=20, pady=5, sticky=W)


        # date label
        date_label = Label(left_inside_label, background="white", text="Date:", font=("times new roman", 12, "bold"))
        date_label.grid(row=2, column=2, padx=10)
        date_Entry = ttk.Entry(left_inside_label, width=20, font=("times new roman", 12, "bold"))
        date_Entry.grid(row=2, column=3, padx=20, pady=5, sticky=W)

        # Attendance status
        atten_label = Label(left_inside_label, background="white", text="Attendance Status", font=("times new roman", 12, "bold"))
        atten_label.grid(row=3, column=0, padx=10)
        atten_combo = ttk.Combobox(left_inside_label, font=("times new roman", 10, "bold"), state="readonly")
        atten_combo["values"] = ("Select Status", "Present", "Absent")
        atten_combo.grid(row=3, column=1, padx=20, pady=10, sticky=W)
        atten_combo.current(0)


        # buttons Frame
        btn_frame = Frame(left_inside_label, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=250, width=690, height=35)


        save_btn = Button(btn_frame, text="Import csv", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",  width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)



        # ==========Right label Frame==========
        right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        right_Frame.place(x=740, y=10, width=720, height= 550)

        table_frame = Frame(right_Frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=705, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll No")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)






if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.resizable(False, FALSE)
    root.mainloop()