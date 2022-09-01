from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

import dataBase
import menu
from PIL import Image, ImageTk
import viewCourses


class edit_Courses:

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
        self.mainFrame = Frame(self.root)
        self.mainFrame.place(x = 0, y = 0, width="800", height="500")

        self.mainFrame1 = Frame(self.root,bg = "white",highlightbackground="white",highlightthickness= 2)
        self.mainFrame1.place(x =0,y = 0,width = "300", height = " 500" )

        self.btn = Button(self.mainFrame1,text="Back",command=self.back,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.btn.place(x =150,y=300, width="100",height= "36")


        self.image = ImageTk.PhotoImage(Image.open('img/course_new.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 150, y =  0,  width="680", height = "500")

        self.banner= Label(self.mainFrame1, text="Edit Courses Items",font = ("Times","21","bold italic"),bg = "white",fg = "black")
        self.banner.place(x = 35, y = 5, width="250")


        self.foodnameLabel = Label(self.mainFrame1, text="Courses Name",bg = 'white',fg = 'black',font = ("Times","14","bold italic"))
        self.foodnameLabel.place(x = 25, y = 80, width="120")

        self.foodnameEntry = Entry(self.mainFrame1,bg = "white")
        self.foodnameEntry.place(x = 25, y = 110, width="215",height= "25")
       
        self.discriptionLabel = Label(self.mainFrame1, text="Courses ID",bg = 'white',fg = 'black',font = ("Times","14","bold italic"))
        self.discriptionLabel.place(x = 25, y = 150, width="120")

        self.discriptionEntry = Entry(self.mainFrame1, bg = "white")
        self.discriptionEntry.place(x = 25, y = 180, width="215",height = "25")

            
        self.submit = Button(self.mainFrame1, text = "Update", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 300, width="100",height= "36")

       

    
        for i in dataBase.editCourses(data):
            print(i)
            self.foodnameEntry.insert(0,i[1])
            self.discriptionEntry.insert(0,i[2])

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()


    def create(self):
       
        data = (
            self.foodnameEntry.get(),
            self.discriptionEntry.get(),
            self.data[0]
            
        )
        if (self.foodnameEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter Food Name')
        elif (self.discriptionEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter Description')
        elif ((self.foodnameEntry.get().isdigit())):
            messagebox.showinfo('Alert', 'Enter Valid Food Name')
        # elif (not(self.priceEntry.get().isdigit())):
            # messagebox.showinfo('Alert', 'Enter valid Price')
        else:
                res  = dataBase.updateCourses_items(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'UPDATE successfully.')
                    self.root.destroy()
                    obj = viewCourses.viewCourses()
                    obj.Courses()
                else:
                    messagebox.showinfo('Alert', 'Please try again.')


if __name__ == '__main__':
    obj =edit_Courses()
    obj.firstFrame("data")
