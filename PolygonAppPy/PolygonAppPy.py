import tkinter as tk
import random
import ctypes
from tkinter import *
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk

bgColors = "gray"


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        container.grid_rowconfigure(0, weight = 1)
        container.columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (MenuPage, OptionsPage, GamePage):
            frame = F(container, self, bg = bgColors)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(MenuPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MenuPage(tk.Frame):
    def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #backColor = OptionsPage.configure(background=color)
        logo = Image.open('logo.png')
        resizedLogo = logo.resize((442,100), Image.ANTIALIAS)
        newLogo = ImageTk.PhotoImage(resizedLogo)
        logo_label = tk.Label(self, image = newLogo)
        logo_label.image = newLogo
        
        #buttons
        gameButton = tk.Button(self, text="Play", command=lambda: controller.show_frame(GamePage), width=10)
        optionsButton = tk.Button(self, text="Options", command=lambda: controller.show_frame(OptionsPage))
        exitButton = tk.Button(self, text="Exit", command=self.quit)
        
        #show Items
        logo_label.grid(row=0, column=0, pady=20, padx=0)
        gameButton.grid(row=1, column=0, pady=(50,0), padx=0)
        optionsButton.grid(row=2, column=0, pady=100, padx=0)
        exitButton.grid(row=3, column=0, pady=(0,100), padx=0)

class OptionsPage(tk.Frame):
        
     def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)
        canvas = tk.Canvas(self, width=600, height=300)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        def change_color():
            colors = askcolor(title="Background Color Chooser")
            self.configure(bg=colors[1])
            #MenuPage.tk.Frame.__init__(MenuPage, Application, bg = colors[1], fg=fg)
            #frame = MenuPage (self.configure(bg=colors[1]))
            #menuPage.configure(bg=colors[1])
            #Frame.configure(bg=colors[1])
            #GamePage.configure()

        #buttons
        backgroundButton = tk.Button(self, text="Background color", command=change_color)
        optBackButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(MenuPage))

        #show Items
        backgroundButton.grid(column=0, row=0)
        optBackButton.grid(column=0, row=1)


class GamePage(tk.Frame):
    def __init__(self, parent, controller, bg=None, fg=None):
        tk.Frame.__init__(self, parent, bg=bg, fg=fg)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        l = tk.IntVar();

        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        def GetBase():
            r=1
        #Definition: da 2K a full hd 1,34. Da full hd a 720 1,5. Da 2k a 720 2.
        a=1504
        b=752
        user32 = ctypes.windll.user32
        if(user32.GetSystemMetrics(0) == 2560 and user32.GetSystemMetrics(1) == 1440):
            a=1000
            b=2000 
        elif(user32.GetSystemMetrics(0) == 1280 and user32.GetSystemMetrics(1) == 720):
            a=1003
            b=501
        
        #Items
        c = Canvas(self, bg="white", height=a, width=b)
        gameBackButton = tk.Button(self, text="Back", command=lambda: controller.show_frame(MenuPage))
        rectangle = tk.Radiobutton(self, text="Rectangle", variable=l, value=0, command=lambda: print(l.get()))
        rectBase = Scale(self, from_=1, to=10, orient=HORIZONTAL, label="Base")
        rectHeight = Scale(self, from_=1, to=10, orient=HORIZONTAL, label="Height")
        triangle = tk.Radiobutton(self, text="Triangle", variable=l, value=0, command=lambda: print(l.get()))
        triBase = Scale(self, from_=1, to=10, orient=HORIZONTAL, label="Base")
        triHeight = Scale(self, from_=1, to=10, orient=HORIZONTAL, label="Height")

        #show Items
        c.grid(sticky="W", row=0, column=0, padx=30, pady=30)
        rectangle.grid(sticky="W", row=1, column=0, padx=30, pady=(30,0))
        rectBase.grid(row=1, column=0, padx=(50.0), pady=(30,0))
        rectHeight.grid(sticky="E", row=1, column=0)
        triangle.grid(sticky="W", row=2, column=0, padx=30, pady=20)
        triBase.grid(row=2, column=0)
        triHeight.grid(sticky="E", row=2, column=0)
        gameBackButton.grid(sticky="E", row=2, column=1, padx=80, pady=40)
        

app = Application()
app.overrideredirect(True)
app.overrideredirect(False)
app.attributes('-fullscreen',True)
app.mainloop()