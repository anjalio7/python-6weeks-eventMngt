from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import dataBase
import menu
class login_page:
    def __init__(self): 
        self.root=Tk()
        self.height=self.root.winfo_screenheight()
        self.width=self.root.winfo_screenwidth()
        self.width=int((self.width-800)/2)
        self.height=int((self.height-500)/2)
        self.root.geometry('800x500+'+str(self.width)+'+'+str(self.height))
        self.root.title("Login Page")

    def log(self):
        self.img=Image.open("img/images.jfif")
        self.resize_img=self.img.resize((400,500))
        self.images=ImageTk.PhotoImage(self.resize_img)
        self.img_lab=Label(self.root,image=self.images)
        self.img_lab.place(x=400,y=0)

        self.fr=Frame(self.root,bg="white")
        self.fr.place(x=0,y=0,width=400,height=500)

        self.lab=Label(self.fr,text="Login Here",bg="white",font=("Bodoni MT",32,"italic"))
        self.lab.place(x=80,y=30)

        self.user=Label(self.fr,text="Username",bg="white",font=("Bodoni MT",25,"italic"))
        self.user.place(x=40,y=120,width=150)

        self.userEntry=Entry(self.fr,bg="white")
        self.userEntry.place(x=60,y=180,width=200,height=25)

        self.password=Label(self.fr,text="Password",bg="white",font=("Bodoni MT",25,"italic"))
        self.password.place(x=40,y=220,width=150)

        self.passwordEntry=Entry(self.fr,bg="white")
        self.passwordEntry.place(x=60,y=280,width=200,height=25)

        self.btn=Button(self.fr,text="Login",command=self.create,bg="white",font=("Bodoni MT",18,"italic"))
        self.btn.place(x=150,y=330,width=100,height=35)

        self.root.mainloop()

    def  create(self):
        self.data=(
            self.userEntry.get(),
            self.passwordEntry.get()
        )

        if(self.userEntry.get()==''):
            messagebox.showinfo('Alert','Enter your username')
        elif(self.passwordEntry.get()==''):
            messagebox.showinfo('Alert','Enter your password')
        else:
            res = dataBase.login(self.data)
            if res:
                messagebox.showinfo("Success","Login successful")
                self.root.destroy()
                obj = menu.menubar()
                obj.firstFrame(res)

            else:
                # print(self.data)
                messagebox.showerror('Alert','Invalid Username/Password')
    
    

if __name__=="__main__":
    obj=login_page()
    obj.log()        

