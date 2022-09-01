from tkinter import *
from PIL import Image, ImageTk
import add_courses,add_department,add_venu,viewEvent_plan
import viewCourses,viewDepartment,viewEvent,viewVenue
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

    def firstFrame(self):

         # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="350", height="500")
        
        self.homeLabel = Label(self.mainFrame, text="WELCOME!",bg = 'white',fg = 'black',font = ("Bell MT",25,"bold italic"),highlightbackground="white",highlightthickness= 1)
        self.homeLabel.place(x = 50, y = 40, width="200")


        # set background image
        self.img=Image.open('img/index2.jpg')
        self.resize_image = self.img.resize((450, 500))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.bgLabel = Label(self.root, image=self.image)
        self.bgLabel.config(bg="white")
        self.bgLabel.place(x = 350, y = 0)
       
       
        menubar=Menu(self.mainFrame)

        # Adding course Menu and commands

        course = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Courses', menu = course)
        course.add_command(label =' Add Course', command = self.openAddcourse)
        course.add_command(label =' Manage Course', command = self.openManagecourse)
        
        # Adding food types Menu and commands

        Department = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Department', menu = Department)
        Department.add_command(label =' Add Department', command = self.opendept)
        Department.add_command(label =' Manage Department', command = self.openManagedept)

        
        Venu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Venu', menu = Venu)
        Venu.add_command(label ='Add Venu', command = self.openAddvenu)
        Venu.add_command(label ='manage Venu', command = self.openManagevenu)
       
        # Adding food Menu and commands
        menubar.add_cascade(label ='Event', command = self.openManageevent)
        menubar.add_cascade(label ='Report Event', command = self.openevent)

        menubar.add_command(label="Logout",command=self.root.quit)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()
        
    def openAddcourse(self):
        self.root.destroy()
        obj =add_courses.add_courses()
        obj.firstFrame()

    def openManagecourse(self):
        self.root.destroy() 
        obj = viewCourses.viewCourses()
        obj.Courses()

    def opendept(self):
        self.root.destroy()
        obj=add_department.login_page()
        obj.log()         

    def openManagedept(self):
        self.root.destroy()
        obj = viewDepartment.viewDepartment()
        obj.Department()

    def openAddvenu(self):
        self.root.destroy()
        obj =add_venu.add_Venue()
        obj.firstFrame()


    def openManagevenu(self):
        self.root.destroy()
        obj = viewVenue.viewVenue()
        obj.Venue()


    def openevent(self):
        self.root.destroy()   
        obj = viewEvent_plan.daily()
        obj.daily_Event()

    def openManageevent(self):
        self.root.destroy()
        obj = viewEvent.viewEvent()
        obj.Event()

if __name__ == '__main__':
    obj = menubar()
    obj.firstFrame()