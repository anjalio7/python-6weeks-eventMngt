from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import editVenue
import dataBase
import viewVenue
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
        
    def Venue(self):
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

        self.tr.heading('#4', text="Edit")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Delete")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        data = dataBase.ViewVenue()
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1],i[2],i[3],"Edit","Delete"))

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width= 800)
        self.root.mainloop() 

       
    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame()
        
    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'col {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#5':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = dataBase.deleteVenue(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = viewVenue()
                    obj.Venue()
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#4':
            self.root.destroy()
            obj = editVenue.edit_Venue()
            obj.firstFrame(gup)
   
if __name__ == '__main__':
    obj = viewVenue()
    obj.Venue()
