from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")


        # first image
        img = Image.open("Images/face2.jpg")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_label = Label(self.root, image = self.photoImg)
        f_label.place(x=0, y=0, width=500, height=130)
        # f_label.pack(fill=X)


        # second image  
        img1 = Image.open("Images/face2.jpg")
        img1 = img1.resize((500,130),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image = self.photoImg1)
        f_label.place(x=500, y=0, width=500, height=130)


        # third image
        img2 = Image.open("Images/face2.jpg")
        img2 = img2.resize((500,130),Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        f_label = Label(self.root, image = self.photoImg2)
        f_label.place(x=1000, y=0, width=500, height=130)


        # background image
        img3 = Image.open("Images/face2.jpg")
        img3 = img3.resize((1510,710),Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image = self.photoImg3)
        bg_img.place(x=0, y=140, width=1510, height=710)


        # title label
        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1510, height=45)


        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=7, y=55, width=1480, height=580)


        # Left Label Frame
        left_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_Frame.place(x=10, y=10, width=720, height= 550)

        img_left = Image.open("Images/face2.jpg")
        img_left = img_left.resize((720,130),Image.LANCZOS)
        self.photoImg_left = ImageTk.PhotoImage(img_left)
        f_label = Label(left_Frame, image = self.photoImg_left)
        f_label.place(x=0, y=0, width=720, height=130)



        # Right Label Frame
        right_Frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_Frame.place(x=740, y=10, width=720, height= 550)


        # Current Course
        current_course_frame = LabelFrame(left_Frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=705, height=150)

        # Department Label
        dep_label = Label(current_course_frame, background="white", text="Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_course_frame, font=("times new roman", 10, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical", "Chemical", "Aerospace")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        # Course Label
        course_label = Label(current_course_frame, background="white", text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10)

        course_combo = ttk.Combobox(current_course_frame, font=("times new roman", 10, "bold"), state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)


        # Year Label
        year_label = Label(current_course_frame, background="white", text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10)

        year_combo = ttk.Combobox(current_course_frame, font=("times new roman", 10, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        # Semester Label
        sem_label = Label(current_course_frame, background="white", text="Semester", font=("times new roman", 12, "bold"))
        sem_label.grid(row=1, column=2, padx=10)

        sem_combo = ttk.Combobox(current_course_frame, font=("times new roman", 10, "bold"), state="readonly")
        sem_combo["values"] = ("Select Semester", "Sem-1", "Sem-2")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)


        # Class Student Information
        class_student_frame = LabelFrame(left_Frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=290, width=705, height=230)






if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.resizable(False, False)
    root.mainloop()