import tkinter as tk
from PIL import Image, ImageTk

class windows(tk.Tk):
    
    #innitialize the class
    def __init__(self, *args, **kwargs):
        #initializes tkinter
        tk.Tk.__init__(self, *args, **kwargs)
        
        # Initializing parent frame as container it is to hold every other thing in the app
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight ="1")
        container.grid_columnconfigure(0, weight ="1")
        
        #this dictionary is going to hold all the frames to be used inn this program
        self.frames = {}
        
        #creating the  irst frame 
        frame = StartPage(container, self)
        
        #passing into the frames dictionary
        self.frames[StartPage] = frame
        
        frame.grid(row=0, column=0 , sticky="nsew")
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()
            
class StartPage(tk.Frame):
    def __init__(self, parent ,controller): 
        tk.Frame.__init__(self,parent)
        self.load = Image.open("doc.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.img =tk.Label(self, image=self.render)
        self.img.image =self.render
        self.img.place(x=0, y=0)
        
        label =tk.Label(self, text="Pharmarcy managment system")
        label.pack(pady=4, padx=4)
        
app = windows()
app.mainloop()

