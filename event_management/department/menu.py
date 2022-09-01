from ast import arg
from tkinter import *
from PIL import Image, ImageTk
import viewVenue
import add_event
import viewEvent
class menubar:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Menu Demonstration')

        # Creating Menubar
        menubar = Menu(self.root)
        
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 800 x 500 is the size of your screen

        self.width = int((self.fullwidth-800)/2)
        self.height=int((self.fullheight-500)/2)

        s = "800x500+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def firstFrame(self,data):
        self.data = data
         # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="350", height="500")
        
        self.homeLabel = Label(self.mainFrame, text="WELCOME!",bg = 'white',fg = 'black',font = ("Bell MT","20","bold italic"),highlightbackground="white",highlightthickness= 1)
        self.homeLabel.place(x = 20, y = 40, width="200")


        # set background image
        self.img=Image.open('img/index2.jpg')
        self.resize_image = self.img.resize((450, 500))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.bgLabel = Label(self.root, image=self.image)
        self.bgLabel.config(bg="white")
        self.bgLabel.place(x = 350, y = 0)
       
       
        menubar=Menu(self.mainFrame)
        
        Event = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Event', menu = Event)
        Event.add_command(label ='Add Event', command = self.openAddEvent)
        Event.add_command(label ='manage Event', command = self.openManageEvent)

        
        Venu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Venu', command = self.openManagefood)
       
        menubar.add_command(label="Logout",command=self.root.quit)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()
    


    def openAddEvent(self):
        self.root.destroy()
        obj =add_event.login_page()
        obj.log(self.data)  

    def openManageEvent(self):
        self.root.destroy()
        obj = viewEvent.viewEvent()
        obj.Event(self.data)

    def openManagefood(self):
        self.root.destroy()
        obj = viewVenue.viewVenue()
        obj.Venue(self.data)
    

if __name__ == '__main__':
    obj = menubar()
    obj.firstFrame('data')