from tkinter import *
import tkinter.messagebox # ===== to display message to the user ======
    # ======= package image library =========
from PIL import Image, ImageTk
from tkinter import ttk

class Systems:
    def __init__(self, master,title):
        # ======== parent class for other classes =======
        self.master = master
        self.title = title
        self.master.title(self.title)
        self.master.geometry('1200x650')

        
        # =========== widgets and variables ===================
    

    def set_bg(self, master):
        self.load = Image.open("images/doc.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.master, image=self.render)
        self.img.image =self.render
        self.img.place(x=0, y=0)

        
        self.lbluser = Label(self.master, text = 'username',  font= ('Helvetica', '10'))
        self.lbluser.place(height = 30,  x =400 , y =200, relwidth= 0.1)

        self.txtuser = Entry(self.master, bd =5, relief = GROOVE, font = (" ", 15))
        self.txtuser.place(height = 30,  x =600 , y = 200)

        self.lblpass = Label(self.master, text = 'password',  font= ('Helvetica', '10'))
        self.lblpass.place(height = 30,  x =400 , y = 280, relwidth= 0.1)

        self.txtpass = Entry(self.master, bd =5, relief = GROOVE, font = (" ", 15))
        self.txtpass.place(height = 30,  x =600 , y = 280)

        self.btnLog = Button(self.master, text = "Login", width = 15, font =('Helvetica', 10),bg = 'blue', fg = 'black' )
        self.btnLog.place(height = 30,  x =400 , y = 350, relwidth= 0.05)

        self.btnReg = Button(self.master, text = "register", width = 15, font =('Helvetica', 10),bg = 'blue', fg = 'black' )
        self.btnReg.place(height = 30,  x =700 , y = 350, relwidth= 0.05)

        self.labeltitle = Label( self.master, text= 'Pharmacy Management System', font =('times new roman', 20, 'bold'), bg = "white" )
        self.labeltitle.place(x = 400 , y = 10)

    # ========= child classes that has methods for my user interfaces ==========



    # ========== register user form =====================

class Login(Systems): f
    def set_label(self):
        pass

class Registration(Systems):
    def set_label(self):
        pass
    
class Recovery_Acc(Systems):
    def test(self):
        pass

    

master = Tk()
window1 =Login(master,' Welcome to Pharmacy Management System')
#window2 = Registration(master,' Registration System')
#window3 = Recovery_Acc(master,'Recovery Account ')
master.configure(background = 'light blue')
window1.set_bg(master)
master.mainloop()

