from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import ttk
import dataBase
import menu
from PIL import Image, ImageTk
import viewEvent
from tkcalendar import DateEntry


class edit_Event:

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
        
    def firstFrame(self,arg,data):
        print(data)
        self.data = data
        self.arg = arg
        print("argsf",arg)
        self.img=Image.open("img/bg1.jpg")
        self.resize_img=self.img.resize((450,500))
        self.images=ImageTk.PhotoImage(self.resize_img)
        self.img_lab=Label(self.root,image=self.images)
        self.img_lab.place(x=350,y=0)

        self.fr=Frame(self.root,bg="white")
        self.fr.place(x=0,y=0,width=350,height=500)

        self.btn = Button(self.fr,text="BACK",command=self.back,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.btn.place(x =200,y=420,width=100,height=36)

        self.lab=Label(self.fr,text="Add Event",bg="white",font=("Bodoni MT",25,"italic"))
        self.lab.place(x=80,y=10)

        self.event=Label(self.fr,text="Event Name",bg="white",font=("Bodoni MT",17,"italic"))
        self.event.place(x=50,y=80,width=150)

        self.eventname=Entry(self.fr,bg="white")
        self.eventname.place(x=60,y=120,width=200,height=25)

        self.user=Label(self.fr,text="Event Date",bg="white",font=("Bodoni MT",17,"italic"))
        self.user.place(x=40,y=160,width=150)

        self.datename=DateEntry(self.fr,date_pattern='yyyy/mm/dd')
        self.datename.delete(0,'end')
        self.datename.place(x=60,y=200,width=200,height=25)

        self.duration=Label(self.fr,text="Duration of event",bg="white",font=("Bodoni MT",18,"italic"))
        self.duration.place(x=40,y=240,width=200)

        self.durationEntry=Entry(self.fr,bg="white")
        self.durationEntry.place(x=60,y=280,width=200,height=25)

        self.venue=Label(self.fr,text="Excepted venue",bg="white",font=("Bodoni MT",18,"italic"))
        self.venue.place(x=40,y=320,width=200)

        self.venueEntry=ttk.Combobox(self.fr,values=(dataBase.ViewVenue()))
        self.venueEntry.place(x=60,y=360,width=200,height=25)

            
        self.submit = Button(self.fr, text = "Update", command=self.create,bg = 'black',fg = 'white',font = ("Times","14","bold italic"))
        self.submit.place(x = 40, y = 420, width="100",height= "36")

       

        val = (arg,self.data[0])
        for i in dataBase.editEvent(val):
            print(i)
            self.eventname.insert(0,i[0])
            self.datename.insert(0,i[1])
            self.durationEntry.insert(0,i[2])
            self.venueEntry.insert(0,(i[3],i[4]))
        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame(self.data)


    def create(self):
        
        self.venueEntry = self.venueEntry.get().split()
        data = (
            self.eventname.get(),
            self.datename.get(),
            self.durationEntry.get(),
            self.venueEntry[0],
            self.arg,
            self.data[0]
            
        )

        if(self.eventname.get()==''):
            messagebox.showinfo('Alert','Enter your event name')
        elif(self.datename.get()==''):
            messagebox.showinfo('Alert','Enter your date of event')
        elif(self.durationEntry.get()==''):
            messagebox.showinfo('Alert','Enter duration of the event')
        elif(self.venueEntry==''):
            messagebox.showinfo('Alert','Enter venue of the event')
        else:
            print(data)
            res  = dataBase.updateEvent_items(data)
            if res:
                messagebox.showinfo('Success', 'UPDATE successfully.')
                self.root.destroy()
                obj = viewEvent.viewEvent()
                obj.Event(self.data)
            else:
                messagebox.showinfo('Alert', 'Please try again.')


if __name__ == '__main__':
    obj =edit_Event()
    obj.firstFrame('arg',"data")
