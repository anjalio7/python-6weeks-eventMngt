from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
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
        
    def Event(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I','J'), selectmode="extended")

        self.btn = Button(self.fr,text="back",command=self.back)
        self.btn.place(x =700,y=450,width=50,height=20)

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Department Name")
        self.tr.column('#1', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#2', text="Course Name")
        self.tr.column('#2', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#3', text="Event Name")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#4', text="Event Date")
        self.tr.column('#4', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#5', text="Event Duration")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#6', text="Exccepted Venue")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#7', text="Status")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#8', text="Accept")
        self.tr.column('#8', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#9', text="Reject")
        self.tr.column('#9', minwidth=0, width=80, stretch=NO)

        val = dataBase.ViewEvent()
        print('val',val)
        if val:
            for i in val:
                print(i)
                self.tr.insert('', 0, text = i[0],tags=i[7], values=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],"Accept","Reject"))
                print("i am 7",i[7])
            
                if i[7]=='pending':
                    self.tr.bind('<Double-Button-1>', self.actions)
        

            self.tr.tag_configure('Reject', background='#FF7F50')
            self.tr.tag_configure('Accept', background='#90ee90')

                # self.tr.tag_bind('pending', ('<Double-Button-1>', self.actions))
            # if i[7]=='Reject':
            #     self.tr.config(state='readonly')
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

        self.gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#9':
            res = messagebox.askyesno("Reject", "Do You Realy Want to Reject this Event.")
            if res:
                a = dataBase.RejectEvent(self.gup)
                if a:
                    self.new_root()
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col=='#8':
            res = messagebox.askyesno("Accept", "Do You Want to Accept this Event.")
            if res:
                a = dataBase.AcceptEvent(self.gup)
                if a:       
                    messagebox.showinfo("Success","Accepted Successfully")
                    self.root.destroy()
                    obj = viewEvent()
                    obj.Event()
                else:
                    messagebox.showinfo("Alert","Something went wrong")
    def new_root(self):
        self.win=Tk()
        self.win.title("Reason")
        self.win.config(bg="white")
        self.win.geometry('300x200+'+'50+'+'50')

        self.reason=Label(self.win,text="Add Reason",bg="white",font=("Bodoni MT",25,"italic"))
        self.reason.place(x=75,y=10)

        self.ReasonEntry=Entry(self.win,bg="white")
        self.ReasonEntry.place(x=25,y=70,width=250,height=50)

        self.btn1 = Button(self.win,text="submit",command=self.value,bg="black",fg="white",font=("Bodoni MT",15,"italic bold"))
        # self.btn1.config(width=100,height=30)
        self.btn1.place(x=100,y=130,width=100,height=30)

        self.win.mainloop()

    def value(self):
        new_res = (self.ReasonEntry.get(),self.gup[0])
        print("new res",new_res)
        if(self.ReasonEntry.get()==''):
            messagebox.showinfo('Alert','Enter your reason')
        else:
            res = dataBase.addReason(new_res)
            if res:
                messagebox.showinfo("Success","Rejected Successfully")
                self.win.destroy()
                self.root.destroy()
                obj = viewEvent()
                obj.Event()
            else:
                messagebox.showinfo("Alert","Something went wrong")

        
if __name__ == '__main__':
    obj = viewEvent()
    obj.Event()
