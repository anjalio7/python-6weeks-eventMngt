from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

import dataBase
import menu
from PIL import Image, ImageTk
import viewVenue


class edit_Venue:

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
        self.btn.place(x =150,y=400, width="100",height= "36")


        self.image = ImageTk.PhotoImage(Image.open('img/course_new.jpg'))
        self.bgLabel = Label(self.mainFrame, image=self.image)
        self.bgLabel.place(x = 150, y =  0,  width="680", height = "500")


        self.mainFrame = Frame(self.root,bg = "white")
        self.mainFrame.place(x = 0, y = 0, width="300", height="500")

        self.btn = Button(self.mainFrame,text="BACK",command=self.back,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.btn.place(x =160,y=400,width=100,height=36)

        self.banner= Label(self.mainFrame, text="Add Venue",font = ("Times",25,"bold italic"),bg = "white",fg = "black")
        self.banner.place(x = 35, y = 15, width="200")

        self.VenueLabel = Label(self.mainFrame, text="Venue Name",bg = 'white',fg = 'black',font = ("Times",18,"bold italic"))
        self.VenueLabel.place(x = 25, y = 100, width=140)

        self.VenueEntry = Entry(self.mainFrame,bg = "white")
        self.VenueEntry.place(x = 25, y = 150, width="215",height= 30)

        self.VenueCodeLabel = Label(self.mainFrame, text="Venue Location",bg = 'white',fg = 'black',font = ("Times",18,"bold italic"))
        self.VenueCodeLabel.place(x = 25, y = 200, width=160)

        self.VenueCodeEntry = Entry(self.mainFrame, bg = "white")
        self.VenueCodeEntry.place(x = 25, y = 250, width="215",height = "25")

        self.VenueCapLabel = Label(self.mainFrame, text="Venue Capacity",bg = 'white',fg = 'black',font = ("Times",18,"bold italic"))
        self.VenueCapLabel.place(x = 25, y = 300, width=160)

        self.VenueCapEntry = Entry(self.mainFrame, bg = "white")
        self.VenueCapEntry.place(x = 25, y = 350, width="215",height = "25")
           
        self.submit = Button(self.mainFrame, text = "Update", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 400, width="100",height= "36")

       

    
        for i in dataBase.editVenue(data):
            print(i)
            self.VenueEntry.insert(0,i[1])
            self.VenueCodeEntry.insert(0,i[2])
            self.VenueCapEntry.insert(0,i[3])

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()


    def create(self):
       
        data = (
            self.VenueEntry.get(),
            self.VenueCodeEntry.get(),
            self.VenueCapEntry.get(),
            self.data[0]
            
        )
        if (self.VenueEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter your Venue Name')
        elif (self.VenueCodeEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter Venue location')
        elif (self.VenueCapEntry.get() == ''):
            messagebox.showinfo('Alert', 'Enter Venue Capacity')
        elif (not(self.VenueCapEntry.get().isdigit())):
            messagebox.showinfo('Alert', 'Enter Valid Capacity')
        else:
                res  = dataBase.updateVenue_items(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'UPDATE successfully.')
                    self.root.destroy()
                    obj = viewVenue.viewVenue()
                    obj.Venue()
                else:
                    messagebox.showinfo('Alert', 'Please try again.')


if __name__ == '__main__':
    obj =edit_Venue()
    obj.firstFrame("data")
