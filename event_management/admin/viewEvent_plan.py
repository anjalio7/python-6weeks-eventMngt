from tkinter import *
from tkinter import messagebox
from turtle import right
import dataBase
import dataBase
from datetime import date,timedelta
import menu
class daily():
    def __init__(self):
        self.root = Tk()
        self.root.title('Today Events')

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()


        self.width = int((self.width-800)/2)
        self.height = int((self.height-500)/2)
        # 'width x height'+ 'x' + 'y'
        s = '800x500+'+str(self.width)+"+"+str(self.height)

        self.root.resizable(height=False,width=False)
        self.root.config(bg="white")
        self.root.geometry(s)
        
        
    def daily_Event(self):

        self.fr = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr.place(x=0, y=0, width="260", height="400")

        self.tit=Label(self.fr,text="Yesterday",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        self.fr1 = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr1.place(x=260, y=0, width="270", height="400")

        self.tit=Label(self.fr1,text="Today",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        self.fr2 = Frame(self.root, bg="white",highlightbackground = "black",highlightthickness = 2, bd=5)
        self.fr2.place(x=530, y=0, width="260", height="400")

        self.tit=Label(self.fr2,text="Tomorrow",bg="white",font=('Cambria',25,'bold'))
        self.tit.pack()

        
        today_date = date.today()
        print("Today was: ",today_date)

        yesterday = today_date - timedelta(days = 1)
        print("Yesterday was: ", yesterday)

        Tomorrow = today_date + timedelta(days = 1)
        print("Tomorrow was: ", Tomorrow)
        # self.btn = Button(self.root,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        # self.btn.place(x =230,y=540,width=150,height=40)
        yesterday = (yesterday,)
        today = (today_date,)
        Tomorrow = (Tomorrow,)

        self.today_view = dataBase.view_today(yesterday)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):              
                self.fr6 = Frame(self.fr,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr6.pack()
                # print(i)

                self.v = IntVar()
                self.text = Label(self.fr6, text = self.today_view[i][1]+" "*3+self.today_view[i][2]+"\n"+self.today_view[i][3],font=("Segoe Script",10,'bold'))
                self.text.config(width=800,height=2,bg="white")
                self.text.pack() 
                
        else:
            self.text = Label(self.fr,text="No Event Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.today_view = dataBase.view_today(today)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):            
                self.fr = Frame(self.fr1,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr.pack()
                # print(i)

                self.v = IntVar()
                self.text = Label(self.fr, text = self.today_view[i][1]+" "*3+self.today_view[i][2]+"\n"+self.today_view[i][3],font=("Segoe Script",10,'bold'))
                self.text.config(width=800,height=2,bg="white")
                self.text.pack() 
                
        else:
            self.text = Label(self.fr1,text="No Event Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.today_view = dataBase.view_today(Tomorrow)
        print(self.today_view)
        if len(self.today_view)>0:
            for i in range(len(self.today_view)):            
                self.fr = Frame(self.fr2,highlightbackground = "black",highlightthickness = 2, bd=0)
                self.fr.pack()
                # print(i)

                self.v = IntVar()
                self.text = Label(self.fr, text = self.today_view[i][1]+" "*3+self.today_view[i][2]+"\n"+self.today_view[i][3],font=("Segoe Script",10,'bold'))
                self.text.config(width=800,height=2,bg="white")
                self.text.pack() 
                

        else:
            self.text = Label(self.fr2,text="No Event Added",font=("Segoe Script",20,'bold'))
            self.text.config(width=260,height=40,highlightbackground = "black", 
                            highlightthickness = 2, bd=0,bg="white")
            self.text.pack()

        self.btn = Button(self.root,text="Back",command=self.back,bg="black",fg="white",font=('Cambria',18))
        self.btn.place(x =350,y=440,width=150,height=40)

        self.root.mainloop()
        
    def create(self):
        pass

    def back(self):
        self.root.destroy() 
        obj = menu.menubar()
        obj.firstFrame() 
        

if __name__ == '__main__':
    obj = daily()
    obj.daily_Event()