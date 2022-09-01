from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import editEvent
import dataBase
import viewEvent
class viewEvent():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('view_Event')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def Event(self,data):
        self.data = data
        print(self.data)
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I','J','K'), selectmode="extended")

        self.btn = Button(self.fr,text="back",command=self.back)
        self.btn.place(x =700,y=450,width=50,height=20)

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        # self.tr.heading('#1', text="Department Name")
        # self.tr.column('#1', minwidth=0, width=80, stretch=NO)

        # self.tr.heading('#2', text="Course Name")
        # self.tr.column('#2', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#1', text="Event Name")
        self.tr.column('#1', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#2', text="Event Date")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#3', text="Event Duration")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Exccepted Venue")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#5', text="Status")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)
        
        self.tr.heading('#6', text="Reason")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="Edit")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#8', text="Delete")
        self.tr.column('#8', minwidth=0, width=80, stretch=NO)

        val = dataBase.ViewEvent(self.data[0])
        print('val',val)
        if val:
            for i in val:
                print(i)
                self.tr.insert('', 0, text = i[0], values=(i[3],i[4],i[5],i[6],i[7],i[8],"Edit","Delete"),tags=i[7])
            self.tr.tag_configure('Reject', background='#FF7F50')
            self.tr.tag_configure('Accept', background='#90ee90')
        

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=500,width= 800)
        self.root.mainloop() 

       
    def back(self):
        self.root.destroy()
        obj =menu.menubar()
        obj.firstFrame(self.data)
        
    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'col {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#8':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                arg = (gup[0],self.data[0])
                print(arg)
                a = dataBase.deleteEvent(arg)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = viewEvent()
                    obj.Event(self.data)
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#7':
            self.root.destroy()
            obj = editEvent.edit_Event()
            obj.firstFrame(gup[0],self.data)
   
if __name__ == '__main__':
    obj = viewEvent()
    obj.Event('data')
