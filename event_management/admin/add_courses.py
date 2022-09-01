from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk
import menu
import viewCourses
import dataBase

class add_courses:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Courses')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)     
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def firstFrame(self):
        self.img=Image.open("img/course_new.jpg")
        self.resize_img=self.img.resize((800,500))
        self.images=ImageTk.PhotoImage(self.resize_img)
        self.img_lab=Label(self.root,image=self.images)
        self.img_lab.place(x=0,y=0)

        self.mainFrame = Frame(self.root,bg = "white")
        self.mainFrame.place(x = 0, y = 0, width="300", height="500")

        self.btn = Button(self.mainFrame,text="BACK",command=self.back,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.btn.place(x =160,y=300,width=100,height=36)

        self.banner= Label(self.mainFrame, text="Add Course",font = ("Times",25,"bold italic"),bg = "white",fg = "black")
        self.banner.place(x = 35, y = 15, width="200")

        self.coursesLabel = Label(self.mainFrame, text="Course Name",bg = 'white',fg = 'black',font = ("Times",18,"bold italic"))
        self.coursesLabel.place(x = 25, y = 100, width=140)

        self.coursesEntry = Entry(self.mainFrame,bg = "white")
        self.coursesEntry.place(x = 25, y = 150, width="215",height= 30)

        self.coursesCodeLabel = Label(self.mainFrame, text="Courses Code",bg = 'white',fg = 'black',font = ("Times",18,"bold italic"))
        self.coursesCodeLabel.place(x = 25, y = 200, width=140)

        self.coursesCodeEntry = Entry(self.mainFrame, bg = "white")
        self.coursesCodeEntry.place(x = 25, y = 250, width="215",height = "25")
            
        self.submit = Button(self.mainFrame, text = "SUBMIT", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 300, width="100",height= "36")

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()
        

    def create(self):

        data = (
            self.coursesEntry.get(),
            self.coursesCodeEntry.get()
       )

        if (self.coursesEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your Food Name')
        elif (self.coursesCodeEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter coursesCode')
        elif ((self.coursesEntry.get().isdigit())):
                messagebox.showinfo('Alert', 'Enter Valid Food Name')
        else:
            res  = dataBase.addCourses(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Courses added successfully.')
                self.root.destroy()
                obj =viewCourses.viewCourses()
                obj.Courses()
            else:
                messagebox.showinfo("Alert","Something went wrong")

if __name__ == '__main__':
    obj =add_courses()
    obj.firstFrame()
