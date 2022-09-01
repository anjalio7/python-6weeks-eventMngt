from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import viewDepartment
import dataBase
import menu
from tkinter import ttk
class login_page:
    def __init__(self):
        self.root=Tk()
        self.height=self.root.winfo_screenheight()
        self.width=self.root.winfo_screenwidth()
        self.width=int((self.width-800)/2)
        self.height=int((self.height-500)/2)
        self.root.geometry('800x500+'+str(self.width)+'+'+str(self.height))
        self.root.title("Add Department")
        self.root.resizable(False,False)
    def log(self):
        self.img=Image.open("img/bg1.jpg")
        self.resize_img=self.img.resize((450,500))
        self.images=ImageTk.PhotoImage(self.resize_img)
        self.img_lab=Label(self.root,image=self.images)
        self.img_lab.place(x=350,y=0)

        self.fr=Frame(self.root,bg="white")
        self.fr.place(x=0,y=0,width=350,height=500)

        self.btn = Button(self.fr,text="BACK",command=self.back,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.btn.place(x =200,y=420,width=100,height=36)

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

        self.btn=Button(self.fr,text="Submit",command=self.create,bg="Black",fg="white",font=("Bodoni MT",18,"italic"))
        self.btn.place(x=80,y=420,width=100,height=35)

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()

    def  create(self):
        data=(
            self.coursename.get(),
            self.HODname.get(),
            self.usernameEntry.get(),
            self.passwordEntry.get()
        )

        if(self.coursename.get()==''):
            messagebox.showinfo('Alert','Enter your course name')
        elif(self.HODname.get()==''):
            messagebox.showinfo('Alert','Enter your HOD Name')
        elif(self.usernameEntry.get()==''):
            messagebox.showinfo('Alert','Enter Username')
        elif(self.passwordEntry.get()==''):
            messagebox.showinfo('Alert','Enter password')
        else:
            res  = dataBase.addDepartment(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Department added successfully.')
                self.root.destroy()
                obj =viewDepartment.viewDepartment()
                obj.Department()
            else:
                messagebox.showinfo("Alert","Something went wrong")



if __name__=="__main__":
    obj=login_page()
    obj.log()        

