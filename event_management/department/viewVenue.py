from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import dataBase
class viewVenue():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('view_Venue')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def Venue(self,data):
        self.data = data
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.btn = Button(self.fr,text="back",command=self.back)
        self.btn.place(x =700,y=450,width=50,height=20)

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Venue Name")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Venue Location")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Capacity")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)


        data = dataBase.viewVenuedata()
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1],i[2],i[3]))

        self.tr.place(x=0, y=0,height=500,width= 800)
        self.root.mainloop() 

       
    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame(self.data)
        
   
if __name__ == '__main__':
    obj = viewVenue()
    obj.Venue('data')
