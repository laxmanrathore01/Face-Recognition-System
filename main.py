from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")
        
        # first image
        img = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoImg = ImageTk.PhotoImage(img)
        f_label = Label(self.root, image = self.photoImg)
        f_label.place(x=0, y=0, width=500, height=130)
        # f_label.pack(fill=X)


        # second image  
        img1 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img1 = img1.resize((500,130),Image.LANCZOS)
        self.photoImg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image = self.photoImg1)
        f_label.place(x=500, y=0, width=500, height=130)


        # third image
        img2 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img2 = img.resize((500,130),Image.LANCZOS)
        self.photoImg2 = ImageTk.PhotoImage(img2)
        f_label = Label(self.root, image = self.photoImg2)
        f_label.place(x=1000, y=0, width=500, height=130)


        # background image
        img3 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face.png")
        img3 = img3.resize((1510,710),Image.LANCZOS)
        self.photoImg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image = self.photoImg3)
        bg_img.place(x=0, y=140, width=1510, height=710)


        # title label
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1510, height=45)


        # Student Detail button
        img4 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\Student Details.jpg")
        img4 = img.resize((220,220),Image.LANCZOS)
        self.photoImg4 = ImageTk.PhotoImage(img4)
        b1 = Button(bg_img, image=self.photoImg4, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Student Details", cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1.place(x=200, y=300, width=220, height=40)



        # Detect Face Button
        img5 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img5 = img.resize((220,220),Image.LANCZOS)
        self.photoImg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img, image=self.photoImg5, cursor="hand2")
        b1.place(x=500, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Face Detector", cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1.place(x=500, y=300, width=220, height=40)



        # Attendance Button
        img6 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img6 = img.resize((220,220),Image.LANCZOS)
        self.photoImg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img, image=self.photoImg6, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Attendance", cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1.place(x=800, y=300, width=220, height=40)



        # Help Button  
        img7 = Image.open(r"C:\Users\BHARAT BHUSHAN\Downloads\Face_Recognition_Images\face2.jpg")
        img7 = img.resize((220,220),Image.LANCZOS)
        self.photoImg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img, image=self.photoImg7, cursor="hand2")
        b1.place(x=1100, y=100, width=220, height=220)

        b1 = Button(bg_img, text="Help Desk", cursor="hand2",font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1.place(x=1100, y=300, width=220, height=40)









if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.resizable(False, False)
    root.mainloop()
