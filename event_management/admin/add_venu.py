from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image, ImageTk
import menu
import viewVenue
import dataBase

class add_Venue:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Add Venue')

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
            
        self.submit = Button(self.mainFrame, text = "SUBMIT", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 400, width="100",height= "36")

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()
        

    def create(self):

        data = (
            self.VenueEntry.get(),
            self.VenueCodeEntry.get(),
            self.VenueCapEntry.get()
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
            res  = dataBase.addVenue(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Venue added successfully.')
                self.root.destroy()
                obj =viewVenue.viewVenue()
                obj.Venue()
            else:
                messagebox.showinfo("Alert","Something went wrong")

if __name__ == '__main__':
    obj =add_Venue()
    obj.firstFrame()
