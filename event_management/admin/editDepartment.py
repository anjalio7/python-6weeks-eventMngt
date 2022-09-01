from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import ttk
import dataBase
import menu
from PIL import Image, ImageTk
import viewDepartment


class edit_Department:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Edit Food Items')

        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def firstFrame(self,data):
        print(data)
        self.data = data
        # create a frame
        self.img=Image.open("img/bg1.jpg")
        self.resize_img=self.img.resize((450,500))
        self.images=ImageTk.PhotoImage(self.resize_img)
        self.img_lab=Label(self.root,image=self.images)
        self.img_lab.place(x=350,y=0)

        self.fr=Frame(self.root,bg="white")
        self.fr.place(x=0,y=0,width=350,height=500)

        self.lab=Label(self.fr,text="Add Department",bg="white",font=("Bodoni MT",25,"italic"))
        self.lab.place(x=80,y=10)

        self.course=Label(self.fr,text="Course Name",bg="white",font=("Bodoni MT",17,"italic"))
        self.course.place(x=50,y=80,width=150)

        self.coursename=ttk.Combobox(self.fr,value=(dataBase.ViewCoursesname()))
        self.coursename.place(x=60,y=120,width=200,height=25)

        self.user=Label(self.fr,text="Department Name",bg="white",font=("Bodoni MT",17,"italic"))
        self.user.place(x=40,y=160,width=200)

        self.HODname=Entry(self.fr,bg="white")
        self.HODname.place(x=60,y=200,width=200,height=25)

        self.username=Label(self.fr,text="Username",bg="white",font=("Bodoni MT",18,"italic"))
        self.username.place(x=40,y=240,width=150)

        self.usernameEntry=Entry(self.fr,bg="white")
        self.usernameEntry.place(x=60,y=280,width=200,height=25)

        self.password=Label(self.fr,text="Password",bg="white",font=("Bodoni MT",18,"italic"))
        self.password.place(x=40,y=320,width=150)

        self.passwordEntry=Entry(self.fr,bg="white")
        self.passwordEntry.place(x=60,y=360,width=200,height=25)

            
        self.submit = Button(self.fr, text = "Update", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 420, width="100",height= "36")

       

    
        for i in dataBase.editDepartment(data):
            print(i)
            self.coursename.insert(0,(i[1],i[2]))
            self.HODname.insert(0,i[3])
            self.usernameEntry.insert(0,i[4])
            self.passwordEntry.insert(0,i[5])
        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()


    def create(self):
        
        self.coursename = self.coursename.get().split()
        data = (
            self.coursename[0],
            self.HODname.get(),
            self.usernameEntry.get(),
            self.passwordEntry.get(),
            self.data[0]
            
        )

        if(self.coursename==''):
            messagebox.showinfo('Alert','Enter your course name')
        elif(self.HODname.get()==''):
            messagebox.showinfo('Alert','Enter your HOD Name')
        elif(self.usernameEntry.get()==''):
            messagebox.showinfo('Alert','Enter Username')
        elif(self.passwordEntry.get()==''):
            messagebox.showinfo('Alert','Enter password')
        else:
                res  = dataBase.updateDepartment_items(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'UPDATE successfully.')
                    self.root.destroy()
                    obj = viewDepartment.viewDepartment()
                    obj.Department()
                else:
                    messagebox.showinfo('Alert', 'Please try again.')


if __name__ == '__main__':
    obj =edit_Department()
    obj.firstFrame("data")
